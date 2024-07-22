from datetime import *
# # datetime module have several classes to work with date and time
# # some of the popular classes defined inside datetime module are :
# # date class : to work with date
# # time class : to work with time
# #  datetime class : combination of date and time classesśś

d1=datetime(2020,5,23,12,45,34,100000)
# print(d1)
# d3=date(2020,1,2)
# print(d3)
d2=date.today()
print(date.today())  #it will return today date only.
print(d1.year)
print(d1.month)
print(d1.day)
print(d2.day)
print(d2.weekday())  #mon 0 sun 6
print(d2.isoweekday()) #mon 1 sun 7
print(d2.isocalendar())

d3=d2.isoformat()

print(type(d3))

date_time = date.fromtimestamp(1887639468)
print("Date from timestamp:", date_time)
# t1=time(12,34)
# # print("qwerty",t1)

t1=time(12,34,25,34566)
t3=time(minute=12,hour=23)
print(t3)
t2=datetime.now()
print(t2)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)
print(t1.microsecond)