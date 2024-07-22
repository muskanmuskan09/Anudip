from cx_Oracle import *
con=connect("system","career")
print(con)
print(con.version)
cur=con.cursor()
print(cur)
L=[[101,'Ajay'],[102,'Reema']]
#eno=int(input("Enter empno:"))
#s=int(input("Enter amount:"))
#cur.execute("create table student1(roll int,name varchar2(20))")
cur.executemany("insert into student1 values(:1,:2)",L)
con.commit()