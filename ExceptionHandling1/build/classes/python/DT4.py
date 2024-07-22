from datetime import datetime
from pytz import *
 
# format = "%Y-%m-%d %H:%M:%S %Z%z"
 
# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
print(now_utc)
 
# Convert to Asia/Kolkata time zone
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
print(now_asia)


# all_timezones
# It returns the list all the available timezones with pytz.all_timezones:

# print(all_timezones)
# print(all_timezones_set)


import pytz
import datetime
from datetime import datetime
 
 
# using localize() function, 
ist = pytz.timezone('Asia/Kolkata')
utc = pytz.timezone('utc')
local_datetime_ist = ist.localize(datetime.now())
local_datetime_utc=utc.localize(datetime.now())
 
print( local_datetime_utc.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print(local_datetime_ist.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
