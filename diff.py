n=int(input("enter the number:"))               #n=10
result=0
for i in range(1,n):                       # repeated inputs
 # different_inputs=int(input("enter the {} different numbers".format(n))) 
    different_inputs=int(input(f"Enter the value for  {i}:  "))
    result=result+different_inputs
print("The result is  ",result)

#>enter the number:10
#enter the 10 different numbers: 