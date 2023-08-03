def magic_square(n):

    magicSquare = []
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)

    i = n//2
    j = n-1

    num=n*n
    count = 1
    while(count<=num):
        if i==-1 and j==n:
            i=0
            j=n-2
        elif i==-1:
            i=n-1
        elif j==n:
            j=0
        elif magicSquare[i][j]!=0:
            j-=2
            i+=1
        else:
            magicSquare[i][j]=count
            #print(count)
            count+=1
            i-=1
            j+=1
    print("Magic Square is")
    for i in range(n):
        a=0
        for j in range(n):
            a+=magicSquare[i][j]
            print(magicSquare[i][j],end='\t')
        print()
    print(f"Sum of each Row/Column/Diagonal is {a}")



#main
s=int(input())
magic_square(s)