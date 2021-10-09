from selenium import webdriver
driver = webdriver.Chrome()

driver.get(r"D:/Python自动化测试/Python/自动化/环境搭建/练习的html/练习的html/弹框的验证/dialogs.html")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='confirm']").click()

driver.switch_to.alert.dismiss() # 取消
        # accept()  确定