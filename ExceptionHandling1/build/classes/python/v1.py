import cx_Oracle
import datetime
conn = cx_Oracle.connect(user='C##892', password='892')
cur = conn.cursor()


# sql="select* from department"
# cur.execute(sql)
# rows=cur.fetchall()
# for i in rows:
#      print(i[0],'{0: <15}'.format(i[1]),'{0: <15}'.format(i[2]))
       
    

sql="select* from employee"
cur.execute(sql)
rows=cur.fetchall()
for i in rows:
      print('{0: <5}'.format(i[0]),'{0: <15}'.format(i[1]),'{0: <5}'.format(i[2]),'{0: <15}'.format(i[3]),'{0: <15}'.format(i[4]),'{0: <15}'.format(i[5]),'{0: <15}'.format(i[6]),'{0: <15}'.format(i[7]),'{0: <20}'.format(i[8]))
   

sql="select* from store"
cur.execute(sql)
rows=cur.fetchall()
for i in rows:
    print('{0: <5}'.format(i[0]),'{0: <15}'.format(i[1]),'{0: <15}'.format(i[2]),'{0: <15}'.format(i[3]),'{0: <15}'.format(i[4]))
          

sql="select* from clothes"
cur.execute(sql)
rows=cur.fetchall()
for i in rows:
    print('{0: <5}'.format(i[0]),'{0: <15}'.format(i[1]),'{0: <15}'.format(i[2]),'{0: <15}'.format(i[3]),'{0: <15}'.format(i[4]))


# sql="select* from sales"
# cur.execute(sql)
# rows=cur.fetchall()
# for i in rows:
#     print(i[0],"   ",i[1],"    ",i[2],"    ",i[3],"    ",i[4])

cur.close()
conn.close()