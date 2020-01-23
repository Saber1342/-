import xlwt
import xlrd

#相对路径读取
data =xlrd.open_workbook("成绩表.xls")

#绝对路径读取
# path='F:/Projects/PythonProjects/小姐姐带你学自动化测试/成绩表.xls'
# file = xlrd.open_workbook(path)

for i in range(0,4):
    table = data.sheets()[i]
    # 通过索引顺序获取
    print(table.name)

print()
table_2 = data.sheet_by_index(1)
#通过索引顺序获取
print(table_2.name)

print()
table_3 =data.sheet_by_name(u'兼容性报表')
print(table_3)

print()
#获取所有行数存储在nrows
nrows = table.nrows
print(nrows)
#获取所有列数存储在ncols
ncols = table.ncols
print(ncols)
