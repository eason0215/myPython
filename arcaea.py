# -*- coding: utf-8 -*-
print('欢迎使用arcaea单曲潜力值计算程序')
dingShu = float(input('请输入定数'))
pts = float(input('请输入分数'))
if pts >= 10000000:
    qianLiZhi = dingShu + 2
elif pts >= 9800000 and pts < 10000000:
    qianLiZhi = dingShu + 1 + (pts - 9800000) / 200000
else:
    qianLiZhi = dingShu + (pts - 9500000) / 300000
if qianLiZhi < 0:
    qianLiZhi = 0
print('你的单曲潜力值是' + str(qianLiZhi))