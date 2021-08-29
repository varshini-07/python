n=int(input("enter the number:"))               
result=0
for i in range(1,n):                       # repeated inputs
    different_inputs=int(input(f"Enter the value for  {i}:  "))
    result=result+different_inputs
print("The result is  ",result)