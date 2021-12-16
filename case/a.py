from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("file:///C:/Users/dell/Desktop/slider.html")

driver.maximize_window()
driver.find_element_by_id('id_username').send_keys("yoyo")
driver.find_element_by_id('id_password').send_keys("123456")
slider = driver.find_element_by_class_name("slider")
# 滑块解锁
action = ActionChains(driver)
action.click_and_hold(slider)    # 按住
action.move_by_offset(248, 0)    # 往右偏移248个像素
action.release()                 # 释放鼠标
action.perform()                 # 执行

# 点登陆按钮
# driver.find_element_by_xpath('//*[@type="submit"]').click()
