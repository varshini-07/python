# Factorial of n nos.
# input n
# factorial of 5=1 * 2*3*4*5=120, i/p :5, o/p : 120

# input n
# fact=1
# for 1 to n
#   fact=fact* i
# print fact
num=int(input("enter the number: "))
fact=1 
for i in range(1,num+1):
    fact=fact*i
print(f"factorial of {num} is",fact)    


