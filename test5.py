from selenium.webdriver.support.select import Select
from selenium import webdriver
import os
from time import sleep
current_dir=os.path.dirname(os.path.abspath(__file__))
chromedriver_dir=current_dir+"\chromedriver.exe"
driver=webdriver.Chrome(chromedriver_dir)
driver.get('https://sahitest.com/demo/selectTest.htm')
s1 = Select(driver.find_element_by_id('s1Id'))
s1.select_by_index(2)
sleep(2)