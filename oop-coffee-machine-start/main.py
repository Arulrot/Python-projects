from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu=Menu()
coffe_maker=CoffeeMaker()
money_mechine=MoneyMachine()


while True:
    print("\nCoffe Mechine ")
    Available_items=menu.get_items()
    choice=input(f"Enter your Required Drink {Available_items} :")
    if choice=="off":
        break
    elif choice=="report":
        report=coffe_maker.report()
        print(report)
    else:
       Available_drink= menu.find_drink(choice)
       resource_sufficeient=coffe_maker.is_resource_sufficient(Available_drink)
       if resource_sufficeient is True:
           if money_mechine.make_payment(Available_drink.cost):
               coffe_maker.make_coffee(Available_drink)