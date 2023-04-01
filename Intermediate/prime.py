a=[55,66,29,44,11]
b=[]

for i in range(0,len(a)):
    if (a[i]>1):
         for j in range(0,i):
            if i%j==0:            
                break
            else:
               b.append(i)
    
print(b)
     


