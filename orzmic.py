# -*- coding: utf-8 -*-
print('欢迎使用orzmic单曲rt计算程序')
dingShu = float(input('请输入定数'))
notes = float(input('请输入物量'))
pts = float(input('请输入分数'))
if pts == 1000000 + notes:
    rt = dingShu + 2.1
elif pts < 1000000 + notes and pts > 1000000:
    rt = dingShu + 2
elif pts == 1000000:
    rt = dingShu + 1.9
elif pts >= 980000 and pts < 1000000:
    rt = dingShu + 1.9 - ((1000000 - pts)* 0.5) / 20000
elif pts >= 950000 and pts < 980000:
    rt = dingShu + 1.4 - ((980000 - pts)* 0.7) / 30000
elif pts >= 900000 and pts < 950000:
    rt = dingShu + 0.7 - ((950000 - pts)* 0.7) / 50000
elif pts >= 700000 and pts < 900000 and dingShu >= 2:
    rt = dingShu - 0.1 - ((900000 - pts)* 1.9) / 200000
elif pts >= 700000 and pts < 900000 and dingShu < 2:
    rt = dingShu - 0.1 - ((900000 - pts)* (dingShu - 0.1)) / 200000
elif pts < 700000:
    rt = 0
print('您的rt是' + rt)