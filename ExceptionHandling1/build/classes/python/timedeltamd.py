# timedelta() method in datetime module
# timedelta --> manipulations on date
from datetime import *
# timedelta(days=value,hours=value,minute =value,seconds=value,microseconds=value,weeks=6)
cd=datetime.now()
print(cd)

new_date=cd+timedelta(days=5,hours=5)
print(new_date)
new_date=cd-timedelta(days=5)

new_date=cd+timedelta(days=5,weeks=1)
print(new_date) #print new_date by adding 12 days 


# it will give diffence in terms of days
diff=cd-new_date
print(diff)
# d1=datetime.now()
# d2=datetime(2023,4,27)
# d3=d2-d1
# print(d3)
# ds=str(d3)
# ds1=str()
# for i in ds:
#     if(i!=" "):
#         ds1=ds1+i
#     else:
#         break
# print(int(ds1))

# d22=datetime.now()
# print(d22)
# print(date.today())
# print(date(2023,3,12))
