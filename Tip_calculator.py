print("Welcome to tip calculator\n")
Bill=float(input("Enter the total bill amount: "))
Tip=float(input("\nHow much do you want to tip the waiter?:"))
People=int(input("\nHow many people to split Bill?:"))
TotalAmount=(Bill+Tip)/People
print("\nEach person should pay :",format(TotalAmount,".2f"))