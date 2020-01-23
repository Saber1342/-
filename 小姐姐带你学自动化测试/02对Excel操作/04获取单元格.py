import xlwt
import xlrd
from xlutils.copy import copy

#单元格添加字体颜色
pattern =xlwt.Pattern()
pattern.pattern =xlwt.Pattern.SOLID_PATTERN
style1 =xlwt.XFStyle()
style1.pattern =pattern
style1 = xlwt.easyxf('pattern: pattern solid, fore_colour red;')

pattern_2 = xlwt.Pattern()
pattern_2.pattern =xlwt.Pattern.SOLID_PATTERN
style2 =xlwt.XFStyle()
style2.pattern_2 =pattern_2
style2 =xlwt.easyxf('pattern: pattern solid, fore_colour blue;')

#相对路径读取
old_data =xlrd.open_workbook("成绩表.xls", formatting_info=True)
table1 =old_data.sheet_by_index(0)#读取第0个表格

#复制excel表格已存在数据
new_data =copy(old_data)
table =new_data.get_sheet(0)

nrows =table1.nrows#统计表格的行数
for i in range(1,nrows):
    score =table1.cell(i,2).value#对应某一列数据
    if score > 60:
        table .write(i,3,'及格',style2)
    else:
        table.write(i,3,'不及格',style1)
#保存
new_data.save('成绩表.xls')
