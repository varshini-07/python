# Fibonacci Series
# 0 1 1 2 3 5....
# Algorithm
# f1=0
# f2=1
# print f1 f2
# for 1 to n
#     result=f1+f2        result=0+1=1,   result=1+1=2
#    swapping is the concept we are going to discuss
#     f1=f2               f1=1            f1=1
#     f2=result           f2=1            f2=2
#     print result
f1=0
f2=1
n=int(input("enter the number: "))
print(f1,'\n',f2)

for i in range(1,n):
    result=f1+f2
    f1=f2
    f2=result
    print(result)
