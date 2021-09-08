from base_page import *
from selenium.webdriver.support.select import Select
def putin_info():
    driver.get('https://ssc.sjtu.edu.cn/f/dae8d35a')
    logging.info('页面加载完成')
    time.sleep(2)
    driver.execute_script("window.stop()")#页面停止加载

    #登陆界面
    try:
        user_id=driver.find_element_by_id("user")
        user_id.send_keys('ChenQQ')
    except AttributeError as e:
        logging.error(e)
        logging.info("重新登陆")
        sys.exit(0)
    user_pass=driver.find_element_by_id("pass")
    user_pass.send_keys('CHEN19960921')

    time.sleep(1)

def putin_code():
    #将验证码转换为字符串
    # driver.maximize_window()

    #截图并保存
    image_dir_01=current_dir+"/01.png"
    driver.save_screenshot(image_dir_01)
    #定位验证码位置及大小
    user_image=driver.find_element_by_id('captcha-img')
    location=user_image.location
    size=user_image.size
    logging.info('验证码位置：%s' %location)
    logging.info('验证码大小：%s' %size)


    #定位截图的位置
    left=int(location['x'])+480 #距离图片左边界距离
    top=int(location['y'])+175 #距离图片上边界距离
    right=left+int(size['width'])+37#左边界+截图宽度
    bottom=top+int(size['height'])+24#上边界+截图高度
    print('验证码的坐标:%d,%d,%d,%d' %(left,top,right,bottom))

    #从文件中读取截图，截取验证码后再次保存
    try:
        img=Image.open(image_dir_01).crop((left,top,right,bottom))
        image_dir_02=current_dir+"/02.png"
        img.save(image_dir_02)
        logging.info('验证码图片截取成功')
    except:
        logging.error('截图尺寸过大')

    #读取验证码图片，并转换成验证码
    # try:
    imageCode = Image.open(image_dir_02) # 图像增强，二值化
    # imageCode.load()
    sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
    image_dir_03=current_dir+"/03.png"
    sharp_img.save(image_dir_03)
    sharp_img.load()  # 对比度增强
    # time.sleep(2)
    code = pytesseract.image_to_string(sharp_img).strip()
    #收到验证码，进行输入验证
    logging.info("验证码是：%s" %code)
    # except:
    #     logging.error('读取验证码失败')

    #填写验证码并登录
    user_check=driver.find_element_by_id("captcha")
    user_login=driver.find_element_by_id("operate-buttons")
    code_2=""
    for i in code.split():
        code_2=code_2+i
    print("code_2 is %s" %code_2)
    user_check.send_keys(code_2)
    user_login.click()
    time.sleep(2)

putin_info()
putin_code()
while True:
    try:
        user_warn=driver.find_element_by_id('div_warn')
        print('-----------------------------验证码错误--------------------------------------')
        logging.info('重新登陆中')
        print('----------------------------------------------------------------------------')
        putin_info()
        putin_code()
    except:
        print('-----------------------------验证码正确--------------------------------------')
        logging.info('正在进入日报填写界面')
        break


def put_teacher():
    """
    填写：对应的思政老师
    右键-检查，快速定位元素位置
    param:
        element1:点击后，打开下拉框——选择‘老师’——再次点击，关闭下拉框；可以获取text属性
        element2：点击后，删除‘老师’
        element3：点击后，选择‘卢丹阳’
    """
    element1=driver.find_element_by_xpath('/html/body/qf-root/qf-pages/qf-app-item/qf-app-initiate/div/div/qf-initiate-apply/div/div[1]/qform-pc-form/div/div[9]/div[1]/qform-pc-form-control/div/div[2]/qform-pc-member/qform-member-accessor/nz-select')
    cur_text=element1.text
    if cur_text=="卢丹阳":
        print("思政老师:%s" %cur_text)
        pass
    else:
        #删除存在的元素
        element2=driver.find_element_by_xpath('/html/body/qf-root/qf-pages/qf-app-item/qf-app-initiate/div/div/qf-initiate-apply/div/div[1]/qform-pc-form/div/div[9]/div[1]/qform-pc-form-control/div/div[2]/qform-pc-member/qform-member-accessor/nz-select/nz-select-top-control/nz-select-item/span[2]')
        element2.click()
        #选择 卢丹阳
        element1.click()
        element3=driver.find_element_by_xpath('/html/body/div[2]/div/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[10]')
        element3.click()
        element1.click()
        cur_text=element1.text
        print("思政老师：%s" %cur_text)

def put_address():
    """
    param:
        element1:点击后，打开下拉框——选择地址——再次点击，关闭下拉框；可以获取text属性
        element2：点击后，选择‘上海市’
        element3:点击后，选择‘上海市’
        element4：点击后，先择‘闵行区’
    预期：
        print：上海市/上海市/闵行区
    """
    element1=driver.find_element_by_xpath('/html/body/qf-root/qf-pages/qf-app-item/qf-app-initiate/div/div/qf-initiate-apply/div/div[1]/qform-pc-form/div/div[11]/div[1]/qform-pc-form-control/div/div[3]/qform-address')
    cur_text=element1.text
    if cur_text=="":
        element1.click()
        time.sleep(1)
        element2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/ul/li[9]')
        element2.click()
        element3=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/ul[2]/li')
        element3.click()
        element4=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/ul[3]/li[8]')
        element4.click()
        element1.click()
        cur_text=element1.text
        print('地址:%s' %cur_text)

def click_submit():
    """
    提交日报
    """
    element1=driver.find_element_by_xpath('/html/body/qf-root/qf-pages/qf-app-item/qf-app-initiate/div/div/qf-initiate-apply/div/div[1]/div[2]/button[2]')
    element1.click()

if __name__=='__main__':
    put_teacher()
    put_address()
    click_submit()
    driver.quit()
    print('日报已提交')