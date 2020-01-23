from selenium import webdriver
import  time

#打开浏览器
str1='C:/Users/MAX/PycharmProjects/untitled2/venv/Scripts/chromedriver.exe'
driver = webdriver.Chrome(str1)

#打开网页
file_path ='file:///F:/Projects/PythonProjects/小姐姐带你学自动化测试/课程参考资料/下拉框组件.html'
driver.get(file_path)
time.sleep(2)

#先定位到下拉框
m=driver.find_element_by_id("ShippingMethod")
#再点击下拉框下的选项
m.find_element_by_xpath("//option[@value='10.69']").click()
print(m.find_element_by_xpath("//option[@value='10.69']").text)
time.sleep(3)
