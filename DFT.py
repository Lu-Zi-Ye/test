import math
import time

a = []
x_re_arr = []
x_im_arr = []
mag = []

for i in range(32):
    a.append(50+100 * math.sin(i/32*2*math.pi) + 110 * math.sin(2*i/32*2*math.pi))

print(len(a))
# print(range(100))

#print("数组为：")
#print(a)
starttime = time.time()

for j in range(32):
    # print(j)
    x_re = 0
    x_im = 0
    for i in range(32):
        x_re += a[i] * math.cos(2 * math.pi * i * j / 32)
        x_im += -1 * a[i] * math.sin(2 * math.pi * i * j / 32)
    #print('x_re[%2d]=%8f\tx_im[%2d]=%8f' % (j, x_re, j, x_im))
    x_re_arr.append(x_re)
    x_im_arr.append(x_im)

print(len(x_re_arr))
print(len(x_im_arr))

#print('Dft结果实部长度：%d' % len(x_re_arr))
#print(x_re_arr)
#print('Dft结果虚部长度：%d' % len(x_im_arr))
#print(x_im_arr)

for i in range(10):
    if i == 0:
        mag_temp = math.sqrt(x_im_arr[i] * x_im_arr[i] + x_re_arr[i] * x_re_arr[i]) / 32
    else:
        mag_temp = math.sqrt(x_im_arr[i] * x_im_arr[i] + x_re_arr[i] * x_re_arr[i]) * 2 / 32
    print('mag[%2d]=%8f' % (i, mag_temp))
    mag.append(mag_temp)

endtime = time.time()

print(endtime - starttime)
