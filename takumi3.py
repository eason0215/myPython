# -*- coding: utf-8 -*-
print('欢迎使用takumi3单曲rating计算程序')
lv = float(input('请输入定数'))
pts = float(input('请输入分数'))
if pts > 999000:
    rt = (lv + 2 + (pts - 999000)/10000)/34
elif pts > 995000:
    rt = (lv + 1.5 + (pts - 995000)/8000)/34
elif pts > 990000:
    rt = (lv + 1 + (pts - 990000)/10000)/34
elif pts > 970000:
    rt = (lv + (pts - 970000)/20000)/34
elif pts > 800000:
    rt = (lv + (pts - 800000)/170000)/34
else:
    rt = 0
print('您的rt是' + rt)