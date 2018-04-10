import jieba
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

# 获取行数,获取列数
num_of_rows = sheet1.nrows
print('Sheet1有 %d 行' % num_of_rows)

jieba.load_userdict('大周词典.txt')             # 加载词典

danmu_data = {}                                 # 存储所有结果
useless_danmu_data = ['的', '，', '<', '>', '=', '[', ']', 'emot']

# 遍历弹幕内容
for i_of_row in range(0, num_of_rows-1):    # 遍历每一条弹幕
    context_of_danmu = sheet1.cell_value(i_of_row, 4)   # 获取当前行的弹幕文本
    cuted_danmu = jieba.lcut(context_of_danmu, cut_all=False)   # 切割文本并存入list
    # 检查并统计切割后list中的所有元素
    for i in range(len(cuted_danmu)):
        #for key in danmu_data:
        if cuted_danmu[i] in useless_danmu_data:
            pass
        elif cuted_danmu[i] not in danmu_data.keys():
            danmu_data[cuted_danmu[i]] = 1
        else:
            danmu_data[cuted_danmu[i]] += 1
# print(danmu_data)

# 生成写入结果的excel
workbook = xlwt.Workbook(encoding='utf-8')
worksheet_word = workbook.add_sheet('词汇统计')

# 词汇统计结果写入excel
i_for_wordcount = 1      # 第0行为标签
for key in danmu_data:
    worksheet_word.write(i_for_wordcount, 0, label='%s' % key)
    worksheet_word.write(i_for_wordcount, 1, label=danmu_data[key])
    i_for_wordcount += 1
i_for_wordcount = 0

# 保存结果工作表(保存为xlsx格式可能会打不开)
# 获取当前时间
file_save_time = time.strftime('%y-%m-%d-%H-%M-%S', time.localtime(time.time()))
workbook.save('词汇统计%s.xls' % file_save_time)

print('Process on excel has been done!')
