from cx_Oracle import *
from csv import *
con=connect("system","career")
cur=con.cursor()
f=open("d:/csvfiles/Dataset-movies.csv","r")
L=list(reader(f))
#print(type(L))
cur.execute("create table movies(sno int,mname varchar2(350),year int,rating float,duration int)")
cur.executemany("insert into movies values(:1,:2,:3,:4,:5)",L)
con.commit()