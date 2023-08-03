#Bubble Sort
l=eval(input('Enter List:'))
for i in range(len(l)-1):
    for j in range(len(l)-i):
        if l[j]>l[j+1]:
            c=l[j]
            l[j]=l[j+1]
            l[j+1]=c
print(l)
