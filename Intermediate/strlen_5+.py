a=['hi','abdul','waseem','nihaal']
b=[]
for i in range(0,len(a)):
    if len(a[i])>5:
        b.append(a[i])
print(b)