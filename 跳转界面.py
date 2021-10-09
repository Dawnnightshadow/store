import  time
from selenium import  webdriver

driver=webdriver.Chrome()
driver.get(r"D:/Python自动化测试/Python/自动化/环境搭建/练习的html/练习的html/跳转页面/pop.html")

driver.maximize_window()
# 最大化的目的： 某些系统是界面适配的，如果缩放或未最大化，有些元素定位不到，无法继续操作

driver.find_element_by_xpath("//*[@id='goo']").click()
time.sleep(3)
#driver.quit()
#driver.close()