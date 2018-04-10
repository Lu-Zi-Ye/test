import math
import time

starttime = time.time()
sourse_arr_re = []
sourse_arr_im = []
butterfly_arr_re = []
butterfly_arr_im = []
mag = []
num_of_arr = 32  # FFT数据量，2的x次方
iteration_times = 0  # 迭代次数
butterfly_distance = 0  # 蝶形运算距离，蝶距
part_distance = 0  # 蝶形运算组距
zeroarr = []
result = []

# 生成数组内容
for i in range(num_of_arr):
    sourse_arr_im.append(0)
    sourse_arr_re.append(
        50 + 100 * math.sin(i / num_of_arr * 2 * math.pi) + 110 * math.sin(2 * i / num_of_arr * 2 * math.pi))
    butterfly_arr_re.append(0)
    butterfly_arr_im.append(0)

'''
# 打印数据源内容
print('sourse_arr长度：%d' % len(sourse_arr_re))
print('sourse_arr_re:', sourse_arr_re)
print('sourse_arr_im:', sourse_arr_im)
print('butterfly_arr长度：%d' % len(butterfly_arr_re))
print('butterfly_arr_re:', butterfly_arr_re)
print('butterfly_arr_im:', butterfly_arr_im)
'''

# 计算迭代次数
num_of_arr_temp = num_of_arr
while num_of_arr_temp > 1:
    num_of_arr_temp = int(num_of_arr_temp / 2)
    iteration_times += 1
#print('共迭代%d次' % iteration_times)

# 进行m = iteration_times次迭代
for i_for_iteration in range(iteration_times):
    m = i_for_iteration + 1
    #print('第%d次迭代：' % m)
    # 计算蝶距
    butterfly_distance = int(num_of_arr / (math.pow(2, m)))
    #print('蝶距：%d' % butterfly_distance)
    # 计算组距
    part_distance = butterfly_distance * 2
    #print('组距：%d' % part_distance)
    # 蝶形运算:
    for i in range(butterfly_distance):     # 第m次迭代中，进行蝶距次计算
        bd = butterfly_distance
        for but_temp in range(int(num_of_arr / part_distance)):   # 在一次蝶距运算中，进行（N/组距）次计算
            k = i + part_distance * but_temp
            j = k + bd
            butterfly_arr_re[k] = sourse_arr_re[k] + sourse_arr_re[j]
            butterfly_arr_im[k] = sourse_arr_im[k] + sourse_arr_im[j]
            r = k << (m - 1)
            WN_re = math.cos(2 * r / num_of_arr * math.pi)
            WN_im = -1 * math.sin(2 * r / num_of_arr * math.pi)
            butterfly_arr_re[j] = (sourse_arr_re[k] - sourse_arr_re[j]) * WN_re - (sourse_arr_im[k] - sourse_arr_im[j]) * WN_im
            butterfly_arr_im[j] = (sourse_arr_re[k] - sourse_arr_re[j]) * WN_im + (sourse_arr_im[k] - sourse_arr_im[j]) * WN_re
    # 蝶形运算结束后，将运算结果覆盖到sourse_arr
    for i in range(num_of_arr):
        sourse_arr_re[i] = butterfly_arr_re[i]
        sourse_arr_im[i] = butterfly_arr_im[i]
    # 清空蝶形运算数组
    #for i in range(num_of_arr):
    #    butterfly_arr_re[i] = 0
    #    butterfly_arr_im[i] = 0
    # 打印本次蝶形运算结果
    #print(sourse_arr_re)
    #print(sourse_arr_im)


for i in range(num_of_arr):
    if i == 0:
        mag_temp = math.sqrt(sourse_arr_im[i] * sourse_arr_im[i] + sourse_arr_re[i] * sourse_arr_re[i]) / num_of_arr
    else:
        mag_temp = math.sqrt(sourse_arr_im[i] * sourse_arr_im[i] + sourse_arr_re[i] * sourse_arr_re[i]) * 2 / num_of_arr
    print('mag[%2d]=%8f' % (i, mag_temp))
    mag.append(mag_temp)

print(mag)

for i in range(10):
    b = i % 4
    c = int(i/4)
    if b == 0:
        result.append(mag[c])
    elif b == 1:
        result.append(mag[c + int(num_of_arr/2)])
    elif b == 2:
        result.append(mag[c + 2])
    elif b == 3:
        result.append(mag[c + int(num_of_arr/2) + 2])

print(result)

# 生成运行时间
endtime = time.time()
print(endtime - starttime)
