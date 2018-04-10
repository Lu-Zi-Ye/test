import xlrd     # 用于读取excel
import xlwt     # 用于写入excel
import time

# 打开目标excel
excelfilename = 'nvliudanmu18-1-21.xlsx'       # 此处定义文件名
sheetbook = xlrd.open_workbook(excelfilename)   # 此处打开工作表
# 生成sheets的引索列表
sheetrange = range(sheetbook.nsheets)
# 打开目标工作表
sheet1 = sheetbook.sheet_by_name("Sheet1")      # 打开表单

# 生成写入结果的excel
workbook = xlwt.Workbook(encoding='utf-8')
worksheet_shuiyoulist = workbook.add_sheet('水友列表')
worksheet_paizilist = workbook.add_sheet('牌子列表')
worksheet_10secdanmu = workbook.add_sheet('10秒弹幕量')
worksheet_result = workbook.add_sheet('统计结果')

# 获取行数,获取列数
num_of_rows = sheet1.nrows
num_of_cols = sheet1.ncols
print('Sheet1有 %d 行,  %d 列' % (num_of_rows, num_of_cols))
worksheet_result.write(0, 0, label='共计接收弹幕条数')
worksheet_result.write(0, 1, label=num_of_rows)

# 获取接收开始时间及结束时间
receive_start_time = time.strftime('%y-%m-%d-%H-%M-%S', time.localtime(sheet1.cell_value(0, 1)))
receive_stop_time = time.strftime('%y-%m-%d-%H-%M-%S', time.localtime(sheet1.cell_value(num_of_rows-1, 1)))
print('接收开始于%s' % receive_start_time)
print('接收结束于%s' % receive_stop_time)
worksheet_result.write(1, 0, label='接收开始于')
worksheet_result.write(1, 1, label='%s' % receive_start_time)
worksheet_result.write(2, 0, label='接收结束于')
worksheet_result.write(2, 1, label='%s' % receive_stop_time)
worksheet_result.write(1, 2, label=(sheet1.cell_value(num_of_rows-1, 1) - sheet1.cell_value(0, 1)) / 60)

# 建立水友字典
dict_of_all_shuiyou = {}
# 字典键对应的值的含义：发言次数，用户等级，牌子名称，牌子等级，牌子房间号
for i_of_row in range(0, num_of_rows-1):    # 遍历每一条弹幕
    shuiyou_name = sheet1.cell_value(i_of_row, 3)
    if shuiyou_name in dict_of_all_shuiyou.keys():
        dict_of_all_shuiyou['%s' % shuiyou_name][0] += 1
    else:
        dict_of_all_shuiyou['%s' % shuiyou_name] = []
        dict_of_all_shuiyou['%s' % shuiyou_name].append(1)
        dict_of_all_shuiyou['%s' % shuiyou_name].append(sheet1.cell_value(i_of_row, 6))  # 用户等级
        dict_of_all_shuiyou['%s' % shuiyou_name].append(sheet1.cell_value(i_of_row, 7))  # 牌子名称
        dict_of_all_shuiyou['%s' % shuiyou_name].append(sheet1.cell_value(i_of_row, 8))  # 牌子等级
        dict_of_all_shuiyou['%s' % shuiyou_name].append(sheet1.cell_value(i_of_row, 9))  # 牌子房间号
# print(dict_of_all_shuiyou)

# 计算总发言水友数量
Count_of_all_fayanshuiyou = len(dict_of_all_shuiyou)
print('一共有 %d 个水友发了弹幕' % Count_of_all_fayanshuiyou)
worksheet_result.write(3, 0, label='水友数量总计')
worksheet_result.write(3, 1, label=Count_of_all_fayanshuiyou)

# 水友列表写入excel
i_for_shuiyoucount = 1      # 第0行为标签
for key in dict_of_all_shuiyou:
    # print(key, dict_of_all_shuiyou[key])
    worksheet_shuiyoulist.write(i_for_shuiyoucount, 0, label='%s' % key)
    worksheet_shuiyoulist.write(i_for_shuiyoucount, 1, label=dict_of_all_shuiyou[key][0])
    worksheet_shuiyoulist.write(i_for_shuiyoucount, 2, label='%s' % dict_of_all_shuiyou[key][1])
    worksheet_shuiyoulist.write(i_for_shuiyoucount, 3, label='%s' % dict_of_all_shuiyou[key][2])
    worksheet_shuiyoulist.write(i_for_shuiyoucount, 4, label='%s' % dict_of_all_shuiyou[key][3])
    worksheet_shuiyoulist.write(i_for_shuiyoucount, 5, label='%s' % dict_of_all_shuiyou[key][4])
    i_for_shuiyoucount += 1
i_for_shuiyoucount = 0

# 写入水友列表第0行标签
worksheet_shuiyoulist.write(0, 0, label='水友ID')
worksheet_shuiyoulist.write(0, 1, label='发言次数')
worksheet_shuiyoulist.write(0, 2, label='斗鱼等级')
worksheet_shuiyoulist.write(0, 3, label='牌子')
worksheet_shuiyoulist.write(0, 4, label='牌子等级')
worksheet_shuiyoulist.write(0, 5, label='牌子房间ID')


# 统计各牌子数量
dict_of_all_paizi = {}
# 字典键值对应的值的含义   牌子名称：牌子数量，牌子房间号
for key in dict_of_all_shuiyou:
    name_of_paizi = dict_of_all_shuiyou['%s' % key][2]
    roomID_of_paizi = dict_of_all_shuiyou['%s' % key][4]
    if name_of_paizi in dict_of_all_paizi.keys():
        dict_of_all_paizi['%s' % name_of_paizi][0] += 1
    else:
        dict_of_all_paizi['%s' % name_of_paizi] = []
        dict_of_all_paizi['%s' % name_of_paizi].append(1)
        dict_of_all_paizi['%s' % name_of_paizi].append(roomID_of_paizi)

# 牌子列表写入excel
i_for_paizicount = 1    # 第0行为标签
for key in dict_of_all_paizi:
    # print(key, dict_of_all_paizi[key])
    worksheet_paizilist.write(i_for_paizicount, 0, label='%s' % key)
    worksheet_paizilist.write(i_for_paizicount, 1, label=dict_of_all_paizi[key][0])
    worksheet_paizilist.write(i_for_paizicount, 2, label='%s' % dict_of_all_paizi[key][1])
    i_for_paizicount += 1
i_for_paizicount = 0

# 写入牌子列表第0行标签
worksheet_paizilist.write(0, 0, label='牌子名称')
worksheet_paizilist.write(0, 1, label='水友数量总计')
worksheet_paizilist.write(0, 2, label='牌子房间ID')

# 统计每10秒弹幕量
fivesec_danmucount = []
danmucount_temp = 0
starttime = sheet1.cell_value(0, 1)
for i_of_row in range(0, num_of_rows-1):
    time_of_current_danmu = sheet1.cell_value(i_of_row, 1)
    if time_of_current_danmu - starttime <= 10:
        danmucount_temp = danmucount_temp + 1
    else:
        fivesec_danmucount.append(danmucount_temp)
        danmucount_temp = 1                 # 此条本身也算一个
        starttime = time_of_current_danmu
fivesec_danmucount.append(danmucount_temp+1)  # 最后一次计数

# 10秒弹幕量写入excel
for i in range(len(fivesec_danmucount)):
    worksheet_10secdanmu.write(i+1, 0, label=i)
    worksheet_10secdanmu.write(i+1, 1, label=fivesec_danmucount[i])

# 写入10秒弹幕量标签
worksheet_10secdanmu.write(0, 0, label='序号')
worksheet_10secdanmu.write(0, 1, label='10sec弹幕量')

# 保存结果工作表(保存为xlsx格式可能会打不开)
# 获取当前时间
result_file_save_time = time.strftime('%y-%m-%d-%H-%M-%S', time.localtime(time.time()))
workbook.save('直播弹幕统计%s.xls' % result_file_save_time)

print('Process on excel has been done!')
