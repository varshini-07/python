basket=[]
num=int(input("how many numbers:"))
for i in range(1,num+1):
    no=input("enter the numbers:")
    basket.append(no)
basket.sort()
print("ascending order: ",basket)
basket.reverse()
print("descending order: ",basket)
#or
basket.sort(reverse=True)
print(basket)

#remove the duplicate values and sorted
basket=[]
num=int(input("how many numbers: "))
for i in range(1,num+1):
    no=int(input("enter the numbers: "))
    basket.append(no)
test=list(set(basket))
test.sort()
print(test)
