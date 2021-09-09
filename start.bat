#python auto.py
#bat 批处理－取年、月、日、时、分、秒、毫秒 
#取年份：echo %date:~0,4% 
#取月份：echo %date:~5,2% 
#取日期：echo %date:~8,2% 
#取星期：echo %date:~10,6% 
#取小时：echo %time:~0,2% 
#取分钟：echo %time:~3,2% 
#取秒：echo %time:~6,2% 
#取毫秒：echo %time:~9,2%

#当时间为8点10分10秒时，运行一次python脚本，并等待2分钟，再次循环

# if %time:~0,2% == 16 if echo %time:~3,2% ==55 if echo %time:~6,2% ==0 (echo this is true else) echo no
:begin

if %time:~0,2% == 8 (
	echo true hour
	goto minute) else (
	echo false hour
	goto begin
	)

:minute
echo check minute
if %time:~3,2% ==10 (
	echo true minute
	python auto.py
	goto pause) else (
	echo false minute
	goto begin)

:pause
TIMEOUT /T 120

goto begin

