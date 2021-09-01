#sum of series
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
num=int(input("enter the number: "))
sum=0
for i in range(1,num+1):
    sum=sum+(i/factorial(i))
print("the sum of series: ",sum)    

#sum of odd n series
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
num=int(input("enter the number: "))
sum=0
for i in range(1,num+1,2):
    sum=sum+(i/factorial(i))
    print(i)
print("sum of series:",sum)    

#sum of even n series
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
# Main
num=int(input("enter the number: "))
sum=0
for i in range(2,num+1,2):
    sum=sum+((i**2)/factorial(i))
    print(i)
print("sum of series:",sum)    
