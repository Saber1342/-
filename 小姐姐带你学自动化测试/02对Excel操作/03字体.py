import xlwt
import xlrd
from xlutils.copy import copy

#创建字体模板
#创建test_font1
test_font1 =xlwt.Font()
#字体为宋体
test_font1.name =u'宋体'
#斜体
test_font1.italic = True
#删除线
test_font1.struck_out =True
#改变字体大小
test_font1.height=400
#赋值style为XFStyle(),初始化样式
style = xlwt.XFStyle()
style.font = test_font1

#相对路径读取，复制excel表格已存在数据
old_data =xlrd.open_workbook("创建表.xls", formatting_info=True)
new_data =copy(old_data)
table =new_data.get_sheet(0)

#往表格填写数据
#sheet.write(row_n,col_n,value)
#在ow_n行col_n列处单元格内写入value值
table.write(0,0,'haha',style)

#保存
new_data.save('创建表.xls')
