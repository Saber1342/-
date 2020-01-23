from selenium import webdriver
import  time

#打开浏览器
str1='C:/Users/MAX/PycharmProjects/untitled2/venv/Scripts/chromedriver.exe'
driver = webdriver.Chrome(str1)

#打开网页
file_path ='file:///F:/Projects/PythonProjects/小姐姐带你学自动化测试/课程参考资料/登录组件.html'
driver.get(file_path)

#定位到输入框清除输入框
driver.find_element_by_id("user_name").clear()
#定位到输入框id输入内容
driver.find_element_by_id("user_name").send_keys("admin")
#设置等待时间
time.sleep(2)

#定位到输入框id清除输入框
driver.find_element_by_id("user_pwd").clear()
#输入内容
driver.find_element_by_id("user_pwd").send_keys("admin")
time.sleep(2)

#定位到提交按钮id 点击提交
driver.find_element_by_id("login_button").click()
time.sleep(2)