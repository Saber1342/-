from selenium import webdriver
import os,time

#打开浏览器
str1='C:/Users/MAX/PycharmProjects/untitled2/venv/Scripts/chromedriver.exe'
driver = webdriver.Chrome(str1)

#打开网页
file_path ='file:///F:/Projects/PythonProjects/小姐姐带你学自动化测试/课程参考资料/弹窗组件.html'
driver.get(file_path)
time.sleep(2)

# #处理alert对话框（显示HelloWorld）
# #获取alert对话框的按钮，点击按钮，弹出alert对话框
# driver.find_element_by_xpath('/html/body/div/input[1]').click()
# #获取alert对话框
# alert =driver.switch_to_alert()
# #添加等待时间
# time.sleep(2)
# #打印警告对话框内容
# print(alert.text)
# #alert对话框属于警告对话框，我们这里只能接受对话框
# alert.accept()
# time.sleep(2)
#

#处理confirm对话框
#获取confirm对话框的按钮点击按钮，弹出confirm对话框
driver.find_element_by_xpath('/html/body/div/input[2]').click()
#获取confirm对话框
dialog_box =driver.switch_to_alert()
time.sleep(2)
#打印警告对话框内容
print(dialog_box.text)
#点击【确认】显示您已确认
dialog_box.accept()
#接受弹窗
print(driver.find_element_by_xpath('//*[@id="textSpan"]/font').text)
time.sleep(2)
#再次获取confirm对话框的按钮，点击按钮，弹出confirm对话框
driver.find_element_by_xpath('/html/body/div/input[2]').click()
#再次获取confirm对话框...
dialog_box = driver.switch_to_alert()
'''点击【取消】显示您未确认'''
time.sleep(2)
#关闭获取取消对话框
dialog_box.dismiss()
print(driver.find_element_by_xpath('*[@id="textSpan"]/font').text)
time.sleep(2)


