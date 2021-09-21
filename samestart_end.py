#function block    
def elements(list):
    count=0
    for term in list:
        if len(term)>1 and term[0]==term[-1]:
            count+=1
    return count
#main block
list=[]
num=int(input("How many elements: "))
for i in range(1,num+1):
    no=input("Enter the Element: ")
    list.append(no)
print("Words: ",list)
print("Words With Same Starting & Ending: ",elements(list))  


