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

