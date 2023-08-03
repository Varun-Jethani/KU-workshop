seq=input()
wordlis=seq.split('#')
wordlis.sort()
new=''
for i in wordlis:
	new=new+i+'#'
new.removesuffix('#')
print(new,end='')
