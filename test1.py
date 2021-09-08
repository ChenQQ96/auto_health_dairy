from base_page import *


logging.info("1")
# get 方法 打开指定网址
try:
    driver.get('http://www.baidu.com')
except:
    logging.error("No such web")

#选择网页元素
try:
    element_keyword = driver.find_element_by_id('kw')
except:
    logging.error("No such element")

#输入字符
try:
    element_keyword.send_keys('宋曲')
except:
    logging.info("failed")

#找到搜索按钮
try:
    element_search_button = driver.find_element_by_id('su')
except:
    logging.info("failed")

element_search_button.click()

import time

#注意这里必须要等待时间，因为代码运行过快，代码运行完的时候页面还没加载出来就会找不到元素

time.sleep(1)

ret = driver.find_element_by_id('1')
print(ret.text)

if ret.text.startswith('宋曲'):#是不是已宋曲开头
    logging.info('通过')
else:
    logging.info('不通过')
# 最后，driver.quit()让浏览器和驱动进程一起退出，不然桌面会有好多窗口
driver.quit()