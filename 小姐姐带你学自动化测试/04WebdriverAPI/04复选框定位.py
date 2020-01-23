from selenium import webdriver
import  time

#打开浏览器
str1='C:/Users/MAX/PycharmProjects/untitled2/venv/Scripts/chromedriver.exe'
driver = webdriver.Chrome(str1)

#打开网页
file_path ='file:///F:/Projects/PythonProjects/小姐姐带你学自动化测试/课程参考资料/复选框组件.html'
driver.get(file_path)
time.sleep(2)

#只勾选单个复选框
driver.find_element_by_id('c2').click()
print(driver.find_element_by_id('c2').text)
time.sleep(3)




