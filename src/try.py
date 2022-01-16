from statistics import StaticsHandler
import time
import datetime


s = StaticsHandler()

d = s.check_time(time.time(), "hour")

   
print(d)
