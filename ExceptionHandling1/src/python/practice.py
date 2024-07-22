# import csv
# f=open("4cse1new.csv","r")
# f1=open("result.csv","w")
# # count=0
# csvreader=list(csv.reader(f))
# csvwriter=csv.writer(f1,lineterminator="\n")
# for i in csvreader:
#     # print(i)
#     if i[2]!='ABS' and i[3]!='ABS' and i[4]!='ABS':
#         print(i)
#         csvwriter.writerow(i)
#         print(csvwriter)
#         # count=count+1
#         # print(count)

# import csv
# f=open("4cse1new.csv","r")
# f1=open("result.csv","w")
# next(f)
# reader_csv=list(csv.reader(f))
# writer_csv=csv.writer(f1,lineterminator="\n")
# for i in reader_csv:
#     if i[2]!='ABS' and i[3]!='ABS' and i[4]!='ABS':
#          marks=int(i[2])+int(i[3])+int(i[4])
#          writer_csv.writerow(str(marks))
#          print(marks)



# import csv
# f=open("dataset-movies.csv","r")
# read=csv.reader(f)
# for i in read:
#     print(i)





import csv
f=open("dataset-movies.csv","r")
f1=open("result.csv","w")
read=list(csv.reader(f))
write=csv.writer(f1)
for i in read:
    if i[1].startswith('The') and i[2]>"1900" and i[3]>"3.8":
        write.writerow(i)
        
        print(i)





# import csv
# f=open("dataset-movies.csv","r")
# f1=open("result.csv","w")
# read=list(csv.reader(f))
# write=csv.writer(f1,lineterminator="\n")
# for i in read:
#     if i[4]>'1200' and i[2]>'1905' and i[2]<'1990' and i[1].startswith('The'):
#         write.writerow(i)
#         print(i)