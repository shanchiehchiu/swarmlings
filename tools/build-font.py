#!/usr/bin/env python3
"""
把像素中文字體「Cubic 11」裁成只含遊戲用到的字，轉成 WOFF2 並用 base64 嵌進 index.html。

為什麼要這樣做：完整字體有 2.8MB，但遊戲只用到約 600 個字。裁剪後約 30KB，
而且嵌在 HTML 裡，遊戲仍然是單一檔案、離線也能用。

用法（需要 fonttools 與 brotli）：
    python3 -m venv .venv && .venv/bin/pip install fonttools brotli
    .venv/bin/python tools/build-font.py

新增或修改遊戲文字後，重新執行一次即可（會自動掃描 index.html 用到的所有字元）。
字體授權：SIL OFL 1.1（見 tools/Cubic11-OFL.txt），來源 https://github.com/ACh-K/Cubic-11
"""
import base64, io, os, re, sys, urllib.request
from fontTools import subset
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(HERE, '..', 'index.html')
TTF = os.path.join(HERE, '.cache', 'Cubic_11.ttf')
URL = 'https://raw.githubusercontent.com/ACh-K/Cubic-11/main/fonts/ttf/Cubic_11.ttf'

if not os.path.exists(TTF):
    os.makedirs(os.path.dirname(TTF), exist_ok=True)
    print('下載字體…'); urllib.request.urlretrieve(URL, TTF)

src = open(HTML, encoding='utf-8').read()
# 只掃「字體標記之外」的文字，避免把上一次嵌入的 base64 也算進去
body = re.sub(r'/\*FONT-BEGIN\*/.*?/\*FONT-END\*/', '', src, flags=re.S)
chars = sorted({c for c in body if ord(c) >= 32} | {chr(i) for i in range(32, 127)})

opt = subset.Options(); opt.flavor = 'woff2'; opt.layout_features = ['*']; opt.name_IDs = ['*']; opt.notdef_outline = True
font = TTFont(TTF)
cmap = font.getBestCmap()
missing = [c for c in chars if ord(c) not in cmap and ord(c) > 127]
sub = subset.Subsetter(opt); sub.populate(text=''.join(chars)); sub.subset(font)
buf = io.BytesIO(); font.flavor = 'woff2'; font.save(buf)
b64 = base64.b64encode(buf.getvalue()).decode()

rule = ("/*FONT-BEGIN*/\n@font-face{font-family:'Cubic11';font-display:block;src:url(data:font/woff2;base64,%s) format('woff2')}\n/*FONT-END*/" % b64)
new = re.sub(r'/\*FONT-BEGIN\*/.*?/\*FONT-END\*/', lambda m: rule, src, flags=re.S)
open(HTML, 'w', encoding='utf-8').write(new)
print('完成：%d 個字元，WOFF2 %.1f KB（base64 後 %.1f KB）' % (len(chars), len(buf.getvalue())/1024, len(b64)/1024))
if missing: print('字體沒有這些字（會退回系統字體）：', ''.join(missing))
