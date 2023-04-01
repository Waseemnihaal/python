a=[4,7,6,8,9]
b=[]
for i in range(0,len(a)):
    if a[i]%3==0:
        b.append(a[i])
print(b)