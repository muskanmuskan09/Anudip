"""a=(12,12)
b=(12,12,)
print(a is b)`
print(id(a))
print(id(b))
print(type(a))
print(type(b))
print(a,'',b)
a=eval(input ("enter a digit : "))
b=eval(input ("enter a digit : "))
print(f'hello {a} {b} ! you are amazing ')
print('{:.0f}'.format(8.0))
print('{:.0f}'.format(8.9))
print('{:.2f}'.format(5.39120))
print('{:.2f}'.format(105.00001121))
print('{:<110}'.format(22.831))
print('{:.}'.format('hello'))"""
a=1
b=2
print("{}-{}".format(a,b))

# NO ERROR in any python version
print("{0}-{1}".format(a,b))