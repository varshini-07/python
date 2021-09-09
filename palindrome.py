str1=input("enter the string: ")
str2=str1[::-1]
print("Given string= ",str1)
print("Reversed string= ",str2)
if (str1==str2):
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")    
    
============================================================================

str1=input("Enter the string: ")
str2=''
index=-1
for i in str1:
        str2+=str1[index]
        index-=1
print("Given string: ",str1)
print("Reversed string: ",str2)        
if(str1==str2):
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")            