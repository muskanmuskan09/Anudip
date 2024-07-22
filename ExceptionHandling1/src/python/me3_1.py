"""dictionary can be created in three ways """

s="APPLE"
def hist(n):
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    print(d) 
hist(s)