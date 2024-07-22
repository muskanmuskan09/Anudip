import csv
import sys
try:
    f=open("Dataset-movie.csv","r")
    f1=open("muskan.csv","w")
    next(f)
    csvreader=csv.reader(f)
    csvwriter=csv.writer(f1,lineterminator="\n")
    for i in csvreader:
        if i not in (None,''):
            if i[2]<'1988' and i[3]=='4.2' and i[4]<'10800':
              print(i)
              csvwriter.writerow(i)
    f.close()
    f1.close()          
except:
    print(sys.exc_info()[0])
else:
    print("No Error Occurs")    
finally:
    print("Code Is Executed ")


import csv
try:
    f=open("Dataset-movies.csv","r")
    read=csv.reader(f)
    data=list(read)
    f1=open("muskan.csv","w")
    write=csv.writer(f1)
    l=[]
    for i in data:
        if i[2] not in(None,'') and i[3] not in(None,'') and i[4] not in(None,''):
            if int(i[2])<1988 and float(i[3])==4.2 and int(i[4])<10800:
                # # l=[i[2],i[3],i[4]]
                # # l.append(i[2],i[3],i[4])
                # write.writerows(i[2],i[3],i[4])
                # # print(l)
                
    f1.close()          
except FileNotFoundError as e:
    print(e)