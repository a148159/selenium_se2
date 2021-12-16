import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://bt-ota-admin-test.beantechyun.cn/#/login")

driver.maximize_window()

us = driver.find_element("xpath", '//*[@placeholder="账户名"]')
us.send_keys("liyan")
psw = driver.find_element("xpath", '//*[@type="password"]')
psw.send_keys("admin123456")

slider = driver.find_element("xpath", '//div[@class="slider"]')
# slider元素坐标
print("slider元素坐标:%s"%slider.location)
action = ActionChains(driver)
action.click_and_hold(slider)
action.move_by_offset(232, 0)    # 往右偏移232个像素
action.perform()
