#Sort
L=eval(input("Enter List:"))
for i in range(len(L)):
    for j in range(i,len(L)):
        if L[j]<L[i]:
            c=L[i]
            L[i]=L[j]
            L[j]=c
print(L)