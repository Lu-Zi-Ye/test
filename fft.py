import math
import time
starttime = time.time()
sourse_arr_re = []
sourse_arr_im = []
WN_re = 0
WN_im = 0
butterfly_arr_re = []
butterfly_arr_im = []
mag = []
temp_re = []
temp_im = []


# 生成WN
def getwnr(j, m):
    r = j << (m - 1)
    #print(r)
    global WN_re
    global WN_im
    WN_re = math.cos(2*r/256*math.pi)
    WN_im = -1*math.sin(2*r/256*math.pi)
    return 0


# 蝶形运算,num是第num次蝶形计算
def butterflycal(re, im, num):
    # 计算两点距离
    butterfly_distance = int(256/(math.pow(2, num)))
    print('butterfly_distance:%d' % butterfly_distance)
    for i_temp in range(butterfly_distance + 1):    # i_temp是行数
        # 计算j_temp,j_temp是蝶形运算的另一行
        j_temp = i_temp + butterfly_distance
        for ii in range(int(256/butterfly_distance) - 1):
            print(ii)
            butterfly_arr_re[i_temp] = re[i_temp + butterfly_distance * ii] + re[j_temp + butterfly_distance * ii]
            butterfly_arr_im[i_temp] = im[i_temp + butterfly_distance * ii] + im[j_temp + butterfly_distance * ii]
            getwnr(i_temp + butterfly_distance * ii - 1, num)
            #print('%d\t%4f\t%4f' % (i_temp, WN_re, WN_im))
            butterfly_arr_re[j_temp + butterfly_distance * ii] = (re[i_temp + butterfly_distance * ii] - re[j_temp + butterfly_distance * ii]) * WN_re - (im[i_temp + butterfly_distance * ii] - im[j_temp + butterfly_distance * ii]) * WN_im
            butterfly_arr_im[j_temp + butterfly_distance * ii] = (re[i_temp + butterfly_distance * ii] - re[j_temp + butterfly_distance * ii]) * WN_im + (im[i_temp + butterfly_distance * ii] - im[j_temp + butterfly_distance * ii]) * WN_re


# 生成数组内容
for i in range(256):
    sourse_arr_im.append(0)
    sourse_arr_re.append(50 + 100 * math.sin(i / 256 * 2 * math.pi) + 110 * math.sin(2 * i / 256 * 2 * math.pi))
    butterfly_arr_re.append(0)
    butterfly_arr_im.append(0)
    temp_re.append(0)
    temp_im.append(0)

print(len(sourse_arr_re))
print(sourse_arr_re)
print(sourse_arr_im)
print(len(butterfly_arr_re))
print(butterfly_arr_re)
print(butterfly_arr_im)

for i in range(8):
    print(i+1)
    #for jtemp in range(256):
    #    temp_re[jtemp] =
    butterflycal(sourse_arr_re, sourse_arr_im, i+1)
    sourse_arr_re = butterfly_arr_re
    sourse_arr_im = butterfly_arr_im
    print(sourse_arr_re)
    print(sourse_arr_im)

for i in range(256):
    if i == 0:
        mag_temp = math.sqrt(sourse_arr_im[i] * sourse_arr_im[i] + sourse_arr_re[i] * sourse_arr_re[i]) #/ 256
    else:
        mag_temp = math.sqrt(sourse_arr_im[i] * sourse_arr_im[i] + sourse_arr_re[i] * sourse_arr_re[i]) #* 2 / 256
    #print('mag[%2d]=%8f' % (i, mag_temp))
    mag.append(mag_temp)


endtime = time.time()
print(endtime - starttime)
