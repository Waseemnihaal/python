a=[22,34,65,33,66]
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i]<a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
print(a[1])