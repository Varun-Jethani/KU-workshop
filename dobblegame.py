#Varun

import string
import random

symbols=[]
symbols=list(string.ascii_letters)
crd1=[0]*5
crd2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)

samesymbol=random.choice(symbols)
symbols.remove(samesymbol)
if (pos1==pos2):
    crd2[pos1]=samesymbol
    crd1[pos2]=samesymbol
else:
    crd1[pos1]=samesymbol
    crd2[pos2]=samesymbol
    crd1[pos2]=random.choice(symbols)
    symbols.remove(crd1[pos2])
    crd2[pos1]=random.choice(symbols)
    symbols.remove(crd2[pos1])
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        albt1=random.choice(symbols)
        symbols.remove(albt1)
        albt2=random.choice(symbols)
        symbols.remove(albt2)
        crd1[i]=albt1
        crd2[i]=albt2
    i+=1
print(crd1,'\n',crd2)
ch=input("Spot Similar Symbol:")
if ch==samesymbol:
    print("Correct Answer")
else:
    print("Wrong Answer")
