运行环境：windows
由于不熟悉centos系统下，无GUI的selenium的用法，本程序主要在windows系统中运行
后续改进：部署在centos系统中
# auto_health_dairy
自动填写健康日报(上海交通大学版)

	1. 健康日报链接：2021年机动学院学生健康日报填报界面 (sjtu.edu.cn)
	2. 网页自动化填写：python网页自动化填写-用python-webdriver实现自动填表_weixin_39784195的博客-CSDN博客
	3. 工具：
		a. Selenium
　　Webdriver:根据浏览器的版本下载
	开发工具
	1. Selenium-webdriver
		a. Selenium WebDriver（一） - 简书 (jianshu.com)
			i. 如何查看谷歌浏览器版本-百度经验 (baidu.com）
			ii. Python3 split() 方法 | 菜鸟教程 (runoob.com)
		b. Selenium - Web自动化测试的基本操作实现 - 简书 (jianshu.com)
		c. python 自动化测试（1）：获取验证码图片，实现自动登录
			i. Anaconda安装OCR——Python tesseract is not installed or it’s not in your path_yangke-CSDN博客
		d. python+selenium 定位隐藏元素
		e. selenium的下拉选择框
快速定位元素的方式：鼠标悬停在目标元素上，右键—检查

运行 start.bat 会每天定时运行运行python文件
运行 stop.bat 会终止所有python进程

