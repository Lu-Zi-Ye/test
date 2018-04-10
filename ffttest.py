import math
import time

starttime = time.time()

target_arr = []
target_arr_even = []
target_arr_odd = []
x_arr_re = []
x_arr_im = []
x_arr_odd_re = []
x_arr_odd_im = []
x_arr_even_re = []
x_arr_even_im = []
xk_arr_re = []
xk_arr_im = []
mag = []

# 生成数组内容
for i in range(256):
    if i < 128:
        target_arr.append(50 + 100 * math.sin(i / 256 * 2 * math.pi) + 110 * math.sin(2 * i / 256 * 2 * math.pi))
    else:
        target_arr.append(50 + 100 * math.sin(i / 256 * 2 * math.pi) + 110 * math.sin(2 * i / 256 * 2 * math.pi))

# print(len(a))
# print(range(100))

# 将数组按奇、偶分开
for i in range(256):
    if i % 2 == 0:  # even
        target_arr_even.append(target_arr[i])
    else:           # odd
        target_arr_odd.append(target_arr[i])

#print("奇数数组长度：%d" % len(target_arr_odd))
#print(target_arr_odd)
#print("偶数数组长度：%d" % len(target_arr_even))
#print(target_arr_even)
#print("完整数组为：")
#print(target_arr)
#print('\n')

# 基2

# 计算奇数数组的dft结果
for j in range(128):
    x_re_temp = 0
    x_im_temp = 0
    for i in range(int(len(target_arr) / 2) - 1):
        x_re_temp += target_arr_odd[i] * math.cos(4 * math.pi * i * j / 256)
        x_im_temp += -1 * target_arr_odd[i] * math.sin(4 * math.pi * i * j / 256)
    # print('x_re[%2d]=%8f\tx_im[%2d]=%8f' % (j, x_re, j, x_im))
    x_arr_odd_re.append(x_re_temp)
    x_arr_odd_im.append(x_im_temp)

#print("x_arr_odd_re数组长度：%d" % len(x_arr_odd_re))
#print(x_arr_odd_re)
#print("x_arr_odd_im数组长度：%d" % len(x_arr_odd_im))
#print(x_arr_odd_im)

# 计算偶数数组的dft结果
for j in range(128):
    # print(j)
    x_re_temp = 0
    x_im_temp = 0
    for i in range(int(len(target_arr) / 2) - 1):
        x_re_temp += target_arr_even[i] * math.cos(4 * math.pi * i * j / 256)
        x_im_temp += -1 * target_arr_even[i] * math.sin(4 * math.pi * i * j / 256)
    # print('x_re[%2d]=%8f\tx_im[%2d]=%8f' % (j, x_re, j, x_im))
    x_arr_even_re.append(x_re_temp)
    x_arr_even_im.append(x_im_temp)
#print(x_arr_even_re)
#print(x_arr_even_im)

# 计算总结果
for i in range(128):
    xk_arr_re_temp = 0
    xk_arr_im_temp = 0
    xk_arr_re_temp += x_arr_odd_re[i]+x_arr_even_re[i]*math.cos(2*math.pi/256)+x_arr_even_im[i]*math.sin(2*math.pi/256)
    xk_arr_im_temp += x_arr_odd_im[i]+x_arr_even_im[i]*math.cos(2*math.pi/256)-x_arr_even_re[i]*math.sin(2*math.pi/256)
    xk_arr_re.append(xk_arr_re_temp)
    xk_arr_im.append(xk_arr_im_temp)

#print('fft结果实部长度：%d' % len(xk_arr_re))
#print(xk_arr_re)
#print('fft结果虚部长度：%d' % len(xk_arr_im))
#print(xk_arr_im)

for i in range(10):
    if i == 0:
        mag_temp = math.sqrt(xk_arr_im[i] * xk_arr_im[i] + xk_arr_re[i] * xk_arr_re[i]) #/ 256
    else:
        mag_temp = math.sqrt(xk_arr_im[i] * xk_arr_im[i] + xk_arr_re[i] * xk_arr_re[i]) #* 2 / 256
    print('mag[%2d]=%8f' % (i, mag_temp))
    mag.append(mag_temp)

endtime = time.time()

print(endtime - starttime)
