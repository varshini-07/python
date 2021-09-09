#sorting using function
def basket_list_asc():
    bucket=[]
    for i in range(1,num+1):
        number=int(input("enter the numbers: "))
        bucket.append(number) 
        bucket.sort()
    return bucket  
# main   
num=int(input("how many numbers: ")) 
# print('Ascending order',basket_list_asc())
b=basket_list_asc()
print ('Ascending values ')
print(b)
def basket_list_desc():
    bucket=[]
    for i in range(1,num+1):
        number=int(input("enter the numbers: "))
        bucket.append(number)
        bucket.sort(reverse=True)
    return bucket
num=int(input("how many numbers: "))
print("descending order",basket_list_desc())          






