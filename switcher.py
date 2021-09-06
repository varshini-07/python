def zero():
    return 'zero'
def one():
    return 'one'
def indirect(i):
    switcher={
        0:zero,
        1:one,
        2:lambda:'two'
            }
    func=switcher.get(i,lambda :'Invalid')
    return func()
print(indirect(4))
print(indirect(2))
print(indirect(1))
==================================================
def length():
    return 'length'
def lower():
    return ("lower")
def upper():
    return ("upper")
def choice(i):
    switch={
        1:length,
        2:lower,
        3:upper,
        4:exit
    }
    fn=switch.get(i,exit)
    return fn()
#Main
while True:
    print("         Menu Items")
    print("         ==========")
    print("         1.  Length")
    print("         2.  Lower")
    print("         3.  Upper")
    print("         4.  Exit")
    ch=int(input("Enter the choice"))
    print(choice(ch))
