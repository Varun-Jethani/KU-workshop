def Transpose(Mat,l):
    t=[]
    v=len(Mat[0])
    for i in range(v):
        x=[]
        for j in range(l):
            x.append(Mat[j][i])
        t.append(x)
    return t      

m=int(input())
M=[]
for i in range(m):
  x=[int(i) for i in input().split()]
  M.append(x)
print(Transpose(M,m),end='')