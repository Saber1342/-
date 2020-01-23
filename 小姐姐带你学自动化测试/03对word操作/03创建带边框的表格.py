import docx
#创建一个word文档，名为file
file = docx.Document('mytest1.docx')
#创建带边框的表格
table =file.add_table(rows=2,cols=2,style='Table Grid')
row =table.rows[0]
row.cells[0].text ='username'
row.cells[1].text ='password'
#第二行
row = table.rows[1]
row.cells[0].text = 'admin'
row.cells[1].text ='123'
#保存为word文档
file.save('mytest1.docx')
