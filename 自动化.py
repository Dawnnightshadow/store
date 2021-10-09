'''
做自动化的前提条件：
1：需求变更的不是特别频发，系统功能不是特别频繁。
2：适用于系统趋于稳定，需求变更不是很频繁的情况下。
环境：
selenium
chromeDriver.exe
 谷歌浏览器：【IE  谷歌  火狐】
'''
import  time
from selenium import  webdriver

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.maximize_window()
# 最大化的目的： 某些系统是界面适配的，如果缩放或未最大化，有些元素定位不到，无法继续操作
driver.find_element_by_id("kw").send_keys("jason jia")

driver.find_element_by_id("su").click()

time .sleep(4)
driver.quit()
#driver.close()


