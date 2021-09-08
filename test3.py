from base_page import *
try:
    driver.get('https://ssc.sjtu.edu.cn/f/dae8d35a')
    logging.info('页面加载完成')
    time.sleep(2)
except: # 捕获超时异常
    logging.info('跳过')
driver.execute_script("window.stop()")#页面停止加载
time.sleep(2)
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
right=left+int(size['width'])+35#左边界+截图宽度
bottom=top+int(size['height'])+23#上边界+截图高度
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
time.sleep(2)
code = pytesseract.image_to_string(sharp_img).strip()
#收到验证码，进行输入验证
logging.info("验证码是：%s" %code)
# except:
#     logging.error('读取验证码失败')

driver.quit()
def get_veri_code():
    pass
