import jieba

jieba.load_userdict('大周词典.txt')

teststr = '大大大'

strresult = jieba.lcut(teststr, cut_all=False)
print(strresult)
#print("/".join(strresult))
