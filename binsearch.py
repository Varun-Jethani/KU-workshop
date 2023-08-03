def binary_search(a,x):
    first_pos = 0
    last_pos = len(a)-1
    flag = 0
    while(first_pos<=last_pos and flag==0):
        mid = (first_pos + last_pos)//2
        if (x==a[mid]):
            flag = 1
            print("The Elment is present at pos:"+str(mid))
            return 
        else:
            if(x<a[mid]):
                last_pos = mid-1
            else:
                first_pos = mid+1
    print("The number is not present")

l=[432,4425,43,4346,23,23,55,234,45,3,34345,34656,477,47477,546,4456,4563,346,46,456,7434,5,64,7456,6456,45,47456,456,36,345,34455,25,23]
l.sort()
binary_search(l,45)