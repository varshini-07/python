def length(str_val):
    return (str(len(str_val)))
def lower(str_val):
    return (str_val.lower())
def upper(str_val):
    return (str_val.upper())

while True:
   
    print("         Menu Items")
    print("         ==========")
    print("         1.  Length")
    print("         2.  Lower")
    print("         3.  Upper")
    print("         4.  Exit")
    ch=int(input("Enter the choice "))
    if(ch>=4) | (ch==0):
        break
    str_value=input("Enter the string value ")
    if (ch==1):
        print("Length is ",length(str_value))
    elif (ch==2):
        print(lower(str_value))
    elif(ch==3):
        print(upper(str_value))

        
        
