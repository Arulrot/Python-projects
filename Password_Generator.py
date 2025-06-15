#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("\nTotal length of the Password :")) 
nr_symbols = int(input("\nHow many symbols would you like?:"))
nr_numbers = int(input("\nHow many numbers would you like?:"))


password=''

if nr_letters<nr_symbols+nr_numbers:
    print("\nYou enterd a invalid input ")
else:
    total_length=nr_letters-nr_symbols-nr_numbers
    for i in range(0,nr_symbols):
        lt=random.choice(symbols)
        password+=lt


    for j in range(0,nr_numbers):
        lt=random.choice(numbers)
        password+=lt
        

    for char in range(0,total_length):
        lt=random.choice(letters)
        password+=lt


    passwordlist=list(password)
    random.shuffle(passwordlist)

    password=''
    for char in passwordlist:
        password+=char

    print("\nYour password is:",password)