import time
import logging
logging.basicConfig(
    # filename='my.log',
    level=logging.INFO,
    format='%(asctime)s %(filename)s +%(lineno)s: %(levelname)-8s %(message)s'
    )
while True:
    time_stamp = time.time()
    # print("时间戳",time_stamp)
    logging.info("时间戳 %s" % time_stamp)
    break
    # sec = 3
    # logging.info("睡眠 %s 秒" % sec)
    # time.sleep(sec)