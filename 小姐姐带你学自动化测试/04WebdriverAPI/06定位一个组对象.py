from selenium import webdriver
import os,time

#打开浏览器
str1='C:/Users/MAX/PycharmProjects/untitled2/venv/Scripts/chromedriver.exe'
driver = webdriver.Chrome(str1)

#打开网页
file_path ='file:///F:/Projects/PythonProjects/小姐姐带你学自动化测试/课程参考资料/复选框组件.html'
driver.get(file_path)
time.sleep(2)

#沟去复选框
checkboxs =driver.find_elements_by_xpath(".//*[@type='checkbox']")
for i in checkboxs:
    i.click()

#打印当前页面上type为checkbox的个数
print(len(driver.find_elements_by_css_selector('input[type=checkbox]')))

#把页面上最后1个chekcbox的沟给去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
