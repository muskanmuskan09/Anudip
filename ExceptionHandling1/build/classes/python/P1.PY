from cx_Oracle import *
con=connect("C##892","892")
print(con)
print(con.version)
cur=con.cursor()
print(cur)
res = cur.execute("Select stu_id from stu1 where stu_fname='DDDD'")
t=cur.fetchall()
for i in t:
    print(i) 

