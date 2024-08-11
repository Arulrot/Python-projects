def addition(a,b):
    return a+b

def subraction(a,b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    return a /b

symbols={
    "+":addition,
    "-":subraction,
    "*":multi,
    "/":divi
}
repeat=True
while repeat is not False:
    print("\nSimple Calculator")
    num1=float(input("\nEnter a number:"))
    print("\nOperation that can be performed are:")
    for symbol in symbols:
        print(symbol)
    operation=input("\nEnter the operation :")
    num2=float(input("\nEnter second number:"))
    ans=symbols[operation](num1,num2)
    print(f"\n{num1} {operation} {num2} = {ans:.2f} ")
    loop=input("\nDo you want to continue 'y' or 'n' :").lower()
    if loop=='y':
        repeat=True
    else:
        repeat=False
