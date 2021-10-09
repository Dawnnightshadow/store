import  time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get(r"D:/Python自动化测试/Python/自动化/环境搭建/练习的html/练习的html/frame.html")
driver.maximize_window()
#driver.find_element_by_id("input1").send_keys("hello ,jason!")
#xpath定位
# 相对定位过滤：driver.find_element_by_xpath("//input[@id='input1']").send_keys("hello ,jaosn!")
# 绝对定位：driver.find_element_by_xpath("/html/body/input").send_keys("hello,jason!")
time.sleep(3)
driver.quit()
