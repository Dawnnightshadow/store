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

driver.get("http://www.jd.com")
driver.maximize_window()
driver.find_element_by_id("key").send_keys("ROG")
driver.find_element_by_xpath("//*[@class='button']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[2]/div/div[1]/a/img").click()
# driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[2]/div/div[1]/a/img").click()

time .sleep(4)
#driver.quit()
#driver.close()


