'''import string
for i in string.ascii_uppercase:
    print(i,end=' ')
print('\n')

for i in string.ascii_lowercase:
    print(i,end=' ')
n=9
for i in range(1,10,2):
    print(i)'''
num = int(input("Enter a number: "))

# If number is greater than 1
if num > 1:
   # Check if factor exist  
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
# Else if the input number is less than or equal to 1
else:
   print(num,"is not a prime number")