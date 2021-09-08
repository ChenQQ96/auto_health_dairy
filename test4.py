from base_page import *
driver.get("https://www.baidu.com")
driver.find_element_by_link_text('登录').click()
time.sleep(1)
driver.find_element_by_link_text('立即注册').click()
time.sleep(1)
driver.find_element_by_name('userName').send_keys('1')