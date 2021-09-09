#fn+F5：调试
#从selenium里面导入webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
from PIL import Image,ImageEnhance
import time
import pytesseract
import sys
import os
#配置logging文件，简化logger = logging.getLogger(__name__)，使用logging.basicConfig定义默认接口，可以直接使用logging对象
import logging
logging.basicConfig(
    # filename='my.log',
    level=logging.INFO,
    format='%(asctime)s %(filename)s +%(lineno)s: %(levelname)-8s %(message)s'
    )

#配置webdriver的路径
import os
current_dir=os.path.dirname(os.path.abspath(__file__))
#chromedriver
chromedriver_dir=current_dir+"\chromedriver.exe"
# logging.info(chromedriver_dir)

#设置启动参数,解决访问Https时不受信任SSL证书问题
option=webdriver.ChromeOptions()
# chrome_options.add_argument('--window-size=1366,768')
option.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"')
option.add_argument('–disable-software-rasterizer')
option.add_argument("service_args=['–ignore-ssl-errors=true','–ssl-protocol=TLSv1']") # Python2/3
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("start-maximized")
option.add_argument("enable-automation")
# option.add_argument("--headless")
# option.add_argument("--no-sandbox")
# option.add_argument("--disable-infobars")
# option.add_argument("--disable-dev-shm-usage")
# option.add_argument("--disable-browser-side-navigation")
# option.add_argument("--disable-gpu")

#指定chrom的驱动
#执行到这里的时候Selenium会到指定的路径将chrome driver程序运行起来
driver = webdriver.Chrome(chromedriver_dir,options=option)
#driver = webdriver.Firefox()#这里是火狐的浏览器运行方法
driver.implicitly_wait(2)
cookies=driver.get_cookies()
driver.set_page_load_timeout(5) # 设置超时时间为5秒，如果5秒后网页还是没有加载完成则抛出异常
