l=[1,2,3,4,3,2,4,5,1,1,1,16,4,7]
s=set(l)
print(s)
for i in s:
    x=l.count(i)
    print("%d occours %d times"%(i,x))
