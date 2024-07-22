# to print date and time we have to import datetime module
from datetime import *

# datetime --> Module
# datetime() --> class
# now() --> method
# datetime.datetime.now() will give current date and time 

x=datetime.now()  #it will return current system date and time
print(x)
print(type(x))
print(type(x.isoformat()))
# creating date --> datetime(y,m,d,h,m,s,ms) 
x=datetime(2023,4,24,13,45,57) #it will return date and time 
print(x)
# >>> here minimum 3 args are compulsory and remaining sets to 0 <<<
# to print only date we can do
print(x.date())

# to print only time we can do
print(x.time())


# the method is called strftime(formating parameter),take one argument format,to specify the format of the returned string.
# it convert datetime object to string object 
# %b month name,short version --> Dec
# %B month name,full version --> January
# %m Month as a number --> 12
# %y year, short version withount centuary --> 18
# %Y year, full version with centuary --> 2018 
# %H hour 00-23 --> 18
# %I hour 00-12 --> 6
# %p AM/PM --> PM
# %M minute 00-59 --> 41
# %a dayname, short version  --> mon
# %A dayname, full version --> monday 
# %S seconds -->45
# %f microseconds (000000 - 999999)--> %f
# %X time --> 23:44:67:567883
# %x date -->2023-02-22
# %w no of weekday --> 1(mon)
# %j day number of year --> 56 


print(datetime.now().strftime("%A"))
print(datetime.now().strftime("%A, %B %d, %Y"))
print(datetime.now().strftime("%b %d, %I%p"))
print(datetime.now().strftime("%x"))
print(datetime.now().strftime("%j"))



# d=x.strftime("%j")  
# print(d)
# print(type(d))  #str
# # b,B,m,y,Y,H,I,p,M,a,A,w,S,f,x,X
#   strptime() -> string parsed time.
print(datetime.strptime("june","%B"))
ds="21 june, 2021"

d1=datetime.strptime(ds,"%d %B, %Y")
print(d1)

# #  it converts seconds to return the corresponding date and time
# print()
