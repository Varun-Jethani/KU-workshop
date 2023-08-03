import string

def encrypt_message(m):
    n=''
    l=string.ascii_lowercase
    u=string.ascii_uppercase

    for i in m:
        if i.isupper():
            i=u[u.index(i)-3]
        elif i.islower():
            i=l[l.index(i)-2]
        n+=i

    return n

Message=input()  
EnMess=encrypt_message(Message) #Encrypt using Function
print(EnMess,end='')