from cx_Oracle import *
con=cx_Oracle.connect("C##892","892")
print(con)
print(con.version)
cur=con.cursor()
print(cur)
res = cur.execute("Select ename from emp where sal:  >3000")
t=cur.fetchall()
for i in t:
    print(i) 