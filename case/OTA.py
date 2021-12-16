import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("http://bt-ota-admin-test.beantechyun.cn/#/login")
driver.maximize_window()
driver.implicitly_wait(5)
us = driver.find_element("xpath", """//div[@class="ivu-form-item-content"]//div[contains(@class,"ivu-input-type-text")]//input[contains(@class,"ivu-input-large")]""")
us.send_keys("liyan")
psw = driver.find_element("xpath", """//div[contains(@class,"ivu-input-type-password")]//input[contains(@class, "ivu-input-large")]""")
psw.send_keys("admin123456")

position1 = driver.find_element("xpath", '//div[@class="slider"]')
position2 = driver.find_element("xpath", '//*[text()="验证通过"]')
ActionChains(driver).drag_and_drop(position1, position2).perform()


# # 显性等待
# # 第一步设置定时器
# wait = WebDriverWait(driver, 20, poll_frequency=0.5)
# # 第二步设置满足的条件,presence_of_element_located等待元素出现
# wait.until(expected_conditions.presence_of_element_located(
#     locator=('xpath', """//div[@class="ivu-form-item-content"]//div[contains(@class,"ivu-input-type-text")]//input[contains(@class,"ivu-input-large")]""")
# ))

# # 弹框确认
# malter = driver.switch_to.alert
# # 点击确认
# malter.accept()


# # 鼠标操作
# # 悬浮
# # 步骤1:移动到设置
# setting = driver.find_element_by_id("")
# # 鼠标悬浮到setting元素
# action_chains = ActionChains(driver)
# action_chains.move_to_element(setting).perform()
# time.sleep(2)
#
# adv_setting = driver.find_element_by_link_text("高级搜素")
# adv_setting.click()


# # 双击
# ac = ActionChains(driver)
# ac.double_click("").perform()
