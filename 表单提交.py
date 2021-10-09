# F:/自动化测试16/练习的html/上传文件和下拉列表/autotest.html
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"D:/Python自动化测试/Python/自动化/环境搭建/练习的html/练习的html/上传文件和下拉列表/autotest.html")

driver.maximize_window()


# 输入用户名
driver.find_element_by_xpath("//*[@id='accountID']").send_keys("贾生")

driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("145862")

driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")

time.sleep(1)

driver.find_element_by_xpath("//*[@id='sexID2']").click()

driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//*[@value='Auterm']").click()

# 上传文件，
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\Users\31459\Pictures\微信图片_20200111133507.jpg")

