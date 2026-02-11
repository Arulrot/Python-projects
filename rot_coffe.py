def tea(stock):
    print("Preparing tea..")
    stock['tea'] -= 1
    stock['milk'] -= 1
    stock['sugar'] -= 1
    print("Tea prepared")

def coffee(stock):
    print("Preparing coffee..")
    stock['coffee'] -= 1
    stock['milk'] -= 1
    stock['sugar'] -= 1
    print("Coffee prepared")

def milk(stock):
    print("Preparing milk..")
    stock['milk']-=1
    print("milk  prepared")

def main():
  stock={'milk':10, 'sugar':10,'tea':10,'coffee':10}
  while True :
    print("Rot Barist ")
    
    print(stock)
    print('''Enter the option
    1-tea
    2-coffe
    3-milk''')
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if stock['tea'] > 0 and stock['milk'] > 0 and stock['sugar'] > 0:
            tea(stock)
        else:
            print("Not enough ingredients for tea!")

    elif choice == 2:
        if stock['coffee'] > 0 and stock['milk'] > 0 and stock['sugar'] > 0:
            coffee(stock)
        else:
            print("Not enough ingredients for coffee!")

    elif choice == 3:
        if stock['milk'] > 0:
            milk(stock)
        else:
            print("Not enough milk!")

    else:
        print("Enter the correct choice..")

main()