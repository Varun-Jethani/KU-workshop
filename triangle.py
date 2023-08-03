n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end='')
    for j in range(i,2*i):
        j=j%10
        print(j,end='')
    for k in range(2*i-2,i-1,-1):
        k=k%10
        print(k,end='')
    print()