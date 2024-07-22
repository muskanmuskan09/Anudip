from cx_Oracle import *
con=connect("system","career")
print(con)
print(con.version)
cur=con.cursor()
print(cur)
en=input("Enter name:")
sal=int(input("Enter salary:"))
res = cur.execute("Select empno,ename,sal from emp where ename=:E and sal>:1",{'1':sal,'E':en})
t=cur.fetchall()
for i in t:
    print(i)