import xlwt

#创建一个表
data = xlwt.Workbook("创建表.xls")
worksheet =data.add_sheet('My Worksheet')
#保存
data.save('创建表.xls')

