n=int(input("enter the number:"))               #n=10
result=0
for i in range(1,n,2):                       # repeated inputs
 # different_inputs=int(input("enter the {} different numbers".format(n))) 
    #different_inputs=int(input(f"Enter the value for  {i}:  "))
    print("The adding value ",i)
    result=result+i
print("The result is  ",result)

#>enter the number:10
#enter the 10 different numbers: 


#range(start,stop,step)
#range(1,n,2)