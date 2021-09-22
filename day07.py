# 1.读取xlrd
# 2.写入xlwt
#   1.步骤
#      1.打开工作簿
#      2.确定哪一个选项卡
#      3.确定表格的XY坐标，才能读取数据
import xlrd
#工作簿
wb = xlrd.open_workbook(filename=r"D:\Python自动化测试\Python\day07\day07【mysql工具类与excel读取】\2020年每个月的销售情况.xlsx")

time=['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']

#求总销售额
#sumz=0
sum = 0
for a in range(0,12):
    sheet = wb.sheet_by_name(time[a])
#获取有多少行，多少列
    rows =sheet.nrows
    #print(rows,"   ",cols)
    for i in range(1,rows):
        data = sheet.row_values(i)
        sum= sum + data[2] *data[4]
    #sumz=sumz+sum
print("总销售总额：",round(sum,2))

#求12个月的总销量
sumz1=0
for a in range(0,12):
    sheet = wb.sheet_by_name(time[a])
#获取有多少行，多少列
    rows =sheet.nrows
    #print(rows,"   ",cols)
    sum1 = 0
    for i in range(1,rows):
        data = sheet.row_values(i)
        sum1= sum1 + data[4]
    sumz1=sumz1+sum1
print("总销售量：",round(sumz1))

#求每种衣服（件数）的占比
#输出所有衣服
bag={}
for a in range(0,12):
    sheet = wb.sheet_by_name(time[a])
#获取有多少行，多少列
    rows =sheet.nrows
    #print(rows,"   ",cols)
    sum1 = 0
    for i in range(1,rows):
        data = sheet.row_values(i)
        if data[1] in bag :
            bag[data[1]]=bag[data[1]]+data[4]
        else :
            bag[data[1]] = data[4]
#print(bag)
print("------------------------------------------")
for name in bag:
    print(name,"的销售量占比为：", round(bag[name] / round(sumz1) * 100,2), "%")
print("------------------------------------------")
money={}
for a in range(0,12):
    sheet = wb.sheet_by_name(time[a])
#获取有多少行，多少列
    rows =sheet.nrows
    #print(rows,"   ",cols)
    sum1 = 0
    for i in range(1,rows):
        data = sheet.row_values(i)
        if data[1] in money:
            money[data[1]] = money[data[1]] + data[4] * data[2]
        else :
            money[data[1]] = data[4] * data[2]

#print(money)
print("------------------------------------------")
for name in money:
    print(name,"的销售额占比为：", round(money[name] / round(sum) * 100,2), "%")
print("------------------------------------------")
p=max(bag.values())
for i in bag.keys():
    if bag[i] ==p:
        print("最畅销的衣服是：", i)
p=min(bag.values())
for i in bag.keys():
    if bag[i] ==p:
       print("全年销量最低的衣服是：", i)

       # book = {}
       # j4 = ("11月", "12月", "1月")
       # for i in j4:  # 第四季度最畅销的衣服是那种
       #     g = zd(book, i)
       # for i in book.keys():
       #     if book[i] == g:
       #         print("第四季度最畅销的衣服是：", i)
time1=("2月", "3月", "4月")
#输出所有衣服
bag={}
for a in range(0,3):
    sheet = wb.sheet_by_name(time1[a])
#获取有多少行，多少列
    rows =sheet.nrows
    #print(rows,"   ",cols)
    sum1 = 0
    for i in range(1,rows):
        data = sheet.row_values(i)
        if data[1] in bag :
            bag[data[1]]=bag[data[1]]+data[4]
        else :
            bag[data[1]] = data[4]
p1=max(bag.values())
for i in bag.keys():
    if bag[i] ==p1:
        print("第一a季度最畅销的衣服是：", i)
time2=("5月", "6月", "7月")
#输出所有衣服
bag={}
for a in range(0,3):
    sheet = wb.sheet_by_name(time2[a])
#获取有多少行，多少列
    rows =sheet.nrows
    #print(rows,"   ",cols)
    sum1 = 0
    for i in range(1,rows):
        data = sheet.row_values(i)
        if data[1] in bag :
            bag[data[1]]=bag[data[1]]+data[4]
        else :
            bag[data[1]] = data[4]
p1=max(bag.values())
for i in bag.keys():
    if bag[i] ==p1:
        print("第二季度最畅销的衣服是：", i)
time3=("8月", "9月", "10月")
#输出所有衣服
bag={}
for a in range(0,3):
    sheet = wb.sheet_by_name(time3[a])
#获取有多少行，多少列
    rows =sheet.nrows
    #print(rows,"   ",cols)
    sum1 = 0
    for i in range(1,rows):
        data = sheet.row_values(i)
        if data[1] in bag :
            bag[data[1]]=bag[data[1]]+data[4]
        else :
            bag[data[1]] = data[4]
p1=max(bag.values())
for i in bag.keys():
    if bag[i] ==p1:
        print("第三季度最畅销的衣服是：", i)
time4=("11月", "12月", "1月")
#输出所有衣服
bag={}
for a in range(0,3):
    sheet = wb.sheet_by_name(time4[a])
#获取有多少行，多少列
    rows =sheet.nrows
    #print(rows,"   ",cols)
    sum1 = 0
    for i in range(1,rows):
        data = sheet.row_values(i)
        if data[1] in bag :
            bag[data[1]]=bag[data[1]]+data[4]
        else :
            bag[data[1]] = data[4]
p1=max(bag.values())
for i in bag.keys():
    if bag[i] ==p1:
        print("第四季度最畅销的衣服是：", i)