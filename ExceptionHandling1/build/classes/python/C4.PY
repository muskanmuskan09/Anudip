from cx_Oracle import *
con=connect("system","career")
print(con)
print(con.version)
cur=con.cursor()
print(cur)
en=input("Enter starting character:")
res = cur.execute("Select empno,ename,sal from emp where ename like :en",(en+'%',))
t=cur.fetchall()
for i in t:
    print(i)