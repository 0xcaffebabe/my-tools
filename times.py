import time
t = time.localtime()
year = t.tm_year
month=t.tm_mon
day=t.tm_mday
hour=t.tm_hour
min=t.tm_min
sec=t.tm_sec
print(str(year)+str(month)+str(day)+str(hour)+str(min)+str(sec))
