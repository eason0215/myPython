# -*- coding: utf-8 -*-
print('欢迎使用phigros单曲rks计算程序')
dingShu = float(input('请输入定数'))
acc = float(input('请输入acc'))
if acc < 70.00:
    rks = 0
elif acc == 70.00:
    rks = dingShu * (1 / 9)
else:
    rks = (((100 * acc - 55) / 45) ** 2) * dingShu
print('你的单曲潜力值是' + str(rks))