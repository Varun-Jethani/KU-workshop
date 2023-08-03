# x=[1,2,3,7,5,6,8,9]
# print(sorted(x)[::-1])
# print(sorted(x,reverse=True))

str1=input("Enter the first string:")
str2=input("Enter the Second String:")
if (sorted(str1)==sorted(str2)):
    print("These are Anagarms")
else:
    print("Not anagrams")