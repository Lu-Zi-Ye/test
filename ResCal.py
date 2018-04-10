import math


Q = 48          # 电机槽数
print('槽数：%d' % Q)

p = 2           # 极对数
print('极对数：%d' % p)

twop = 2 * p    # 极数
print('极数：%d' % twop)

tao = Q / twop  # 极距
print('极距：%d' % tao)

y = 11 - 1      # 节距
print('节距：%d' % y)

ang_mech_percao = 360 / Q
print('每槽机械角度：%f' % ang_mech_percao)

ang_mech_perji = 360 / twop
print('每极机械角度：%f' % ang_mech_perji)

ang_ele_percao = ang_mech_percao * twop
print('每槽电角度：%f' % ang_ele_percao)

a = ang_ele_percao
print('槽距角（每槽电角度）：%f' % a)

q = Q / (twop * 3)
print('每极每相槽数：%d' % q)

halflenthinaverage = 350    # 平均半匝长，单位mm
print('平均半匝长：%fmm' % halflenthinaverage)

zashu = 31                  # 匝数
print('匝数：%d' % zashu)

numofparallelconductors = 4     # 并联支路数
print('并联支路数：%d' % numofparallelconductors)

totallenth = halflenthinaverage * zashu * 2 * twop / numofparallelconductors
print('导体总长：%d' % totallenth)

conductivity = 58000    # 铜线导电率，单位西门子每mm
print('铜线导电率：%d' % conductivity)

faiofconductor = 0.95
bingraoxian = 2
print('%d线并绕' % bingraoxian)
print('铜线直径%f' % faiofconductor)

totalareaofconductor = bingraoxian * math.pi * (faiofconductor / 2) * (faiofconductor / 2)
print('铜线截面积%f' % totalareaofconductor)

totalR = totallenth / (conductivity * totalareaofconductor)
print('总电阻%f' % totalR)
