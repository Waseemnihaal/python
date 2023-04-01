a=['waseem','abdul','nihaal','xyz']
for i in range (0,len(a)):
    for j in range(i,len(a)):
        if a[i]> a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
print(a)