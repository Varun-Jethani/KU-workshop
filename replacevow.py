def replaceV(x):
    V="aeiouAEIOU"
    vc=0
    l=''
    n=''
    for i in range(len(x)):
        if x[i] in V:
            vc+=1
            l+=x[i]
        else:
            vc=0
            n+=l
            n+=x[i]
            l=''
        if vc==3:
            l=''
            n+='_'
            vc=0
    n+=l
    return n

s=input()
print(replaceV(s),end='')





