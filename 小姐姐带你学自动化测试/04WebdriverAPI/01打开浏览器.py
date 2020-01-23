from selenium import webdriver
import  time
str='C:/Program Files (x86)/Google/Chrome/Application/chrome_proxy.exe'
str1='C:/Users/MAX/PycharmProjects/untitled2/venv/Scripts/chromedriver.exe'
driver = webdriver.Chrome(str)

driver.get("https://www.baidu.com/")

driver.maximize_window()
time.sleep(3)
