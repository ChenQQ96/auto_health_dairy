from base_page import *

#访问天气查询网站（网址如下），查询江苏省天气
# http://www.weather.com.cn/html/province/jiangsu.shtml
# 获取江苏所有城市的天气，并找出其中每天最低气温最低的城市，显示出来，比如
# 温度最低为12℃, 城市有连云港 盐城

driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')
element=driver.find_element_by_id("forecastID")
# logging.info(element.text)

citys_weather=element.text.split('℃\n')

lowest_temp=None
lowest_citys=[]
# logging.info(type(lowest_temp))


for i in citys_weather:
    i=i.replace('℃','')
    parts=i.split('\n')#split('分隔符'),返回的是数组
    cur_city=parts[0]
    # logging.info(cur_city)
    low_weather=int(parts[1].split('/')[0])
    # logging.info(low_weather)
    # #另一种写法：数组元素为int
    # low_weather=min([int(i) for i in parts[1].split('/')])
    # #另一种写法：字符串比大小
    # low_weather=int(min(parts[1].split('/')))
    # logging.info(type(low_weather))

    #lowest_temp为None，或者low_weather<lowest_temp
    #更新结果
    if lowest_temp==None or low_weather < lowest_temp:
        lowest_temp=low_weather
        lowest_citys=[cur_city]
    
    #lowest_temp==lowest_weather
    #添加结果
    elif lowest_temp==low_weather:
        lowest_citys.append(cur_city)

#数组转字符串，并设置间隔符的用法
logging.info("最低温度是%d℃，城市有%s" %(lowest_temp,','.join(lowest_citys)))

driver.quit()