def largest_zero_streak(s):
    st=0
    lst=[]
    for i in s:
        if i=='0':
            st+=1
        else:
            lst.append(st)
            st=0
    lst.append(st)
    return max(lst)
s=input()
print(largest_zero_streak(s),end='')
