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

