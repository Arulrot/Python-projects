import time

menu = {
    "latte": {
        "ingredients": {
            "water": 200,  # ml
            "milk": 150,    # ml
            "coffee": 24   # grams
        },
        "cost": 2.5      # currency units
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,  # ml
            "milk": 100,    # ml
            "coffee": 24   # grams
        },
        "cost": 3.5       # currency units
    },
    "espresso": {
        "ingredients": {
            "water": 50,    # ml
            "coffee": 18   # grams
        },
        "cost": 1.5        # currency units
    }
}

profit=0
resourses={
    "water":1000,
    "milk":500,
    "coffee":100
}


def is_resource_sufficient(order_ingredients):
    all_sufficient=True
    for item in order_ingredients:
        if order_ingredients[item] > resourses[item]:
            print("Not Sufficient resource " ,item)
            all_sufficient=False
    
    return all_sufficient


def coin_Processing(drink,cost):
    print(f"The cost of {drink} would be {cost}")
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def is_transcation_success(money_recived,cost_of_drink):
    if money_recived >= cost_of_drink:
        change=round(money_recived-cost_of_drink,2)
        if change!=0:
            print(f'The remaining change for your drink is {change}')
        global profit
        profit+=cost_of_drink
        

        return True
    else:
        print("Sorry not enough Money ")
        return False
            
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resourses[item] -=order_ingredients[item]
    print(f"\nProcessing your {drink_name}",end="")
    for _ in range(3):
        time.sleep(1)
        print(".",end="",flush=True)

    print(f"\nHere is your {drink_name}")




def main():
    try:
        while True:
            print("\nCoffe Mechine")
            choice=input("Would you like Cappucino/espresso/latte ? : ").lower()
            if choice=='off':
                break
            elif choice=='report':
                print("\nAvailable Resources ")
                print(f"water :{resourses['water']}")
                print(f"coffee :{resourses['coffee']}")
                print(f"milk :{resourses['milk']}")
                print(f"profit :",profit)

                continue

            else:
                drink=menu[choice]
                if is_resource_sufficient(drink["ingredients"]):
                    payment=  coin_Processing(choice,drink["cost"])
                    if is_transcation_success(payment,drink["cost"]):
                        make_coffee(choice,drink["ingredients"])
    except KeyError:
        print("\nYou Might entered a wrong input , Please Enter the correct input")
        main()           
            






main()