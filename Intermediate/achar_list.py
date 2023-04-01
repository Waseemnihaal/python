a=['waseem','xyz','pack','err']
b=[]
for i in range(0,len(a)):
    for j in a[i]:
        if j=='a':
            b.append(a[i])
print(b)
