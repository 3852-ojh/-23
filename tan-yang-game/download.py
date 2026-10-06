# -*- coding: utf-8 -*-
import urllib.request, os

base = r"C:\Users\Administrator\Doubao\chats\2026-10-06\new-chat\tan-yang-game\assets"
imgs = {
    "tan_1.jpg":  "https://aka.doubaocdn.com/s/jhVjbEiHMU",   # 滩羊 双胞胎黑头白身卷毛
    "tan_2.jpg":  "https://aka.doubaocdn.com/s/0jHCTOSLjv",   # 滩羊 母羊+羊羔 黑斑白蓬松
    "tan_3.jpg":  "https://aka.doubaocdn.com/s/5UJUuoIAbT",   # 滩羊 两只黑脸草地
    "tan_4.jpg":  "https://aka.doubaocdn.com/s/UmhwBlap4d",   # 待确认 卷毛白绵羊
    "tan_herd.jpg":"https://aka.doubaocdn.com/s/581VkLklb8",  # 滩羊 山坡羊群
    "sheep_1.jpg":"https://aka.doubaocdn.com/s/nWLcJ7KiO8",   # 普通绵羊 白底纯白
    "sheep_2.jpg":"https://aka.doubaocdn.com/s/DDhPbM0VCk",   # 普通绵羊 白底正面
    "goat_1.jpg": "https://aka.doubaocdn.com/s/ReQkXVLgbO",   # 山羊 棕褐黑胡须
    "goat_2.jpg": "https://aka.doubaocdn.com/s/gVFjoeJ8Xt",   # 山羊 头部特写
    "goat_3.jpg": "https://aka.doubaocdn.com/s/751f96c7c0dc5b0e1e86c67e90129c83", # 黑山羊
    "wool_1.jpg": "https://aka.doubaocdn.com/s/qcwHzKNT6s",   # 羊毛纹理
}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
for name, url in imgs.items():
    path = os.path.join(base, name)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as r, open(path, "wb") as f:
            f.write(r.read())
        print("OK", name, os.path.getsize(path))
    except Exception as e:
        print("FAIL", name, repr(e))
