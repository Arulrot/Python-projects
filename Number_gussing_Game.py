import random

total_chance=0
guessed_numbers=[]

computer_number=random.randint(1,101)
print(computer_number)
def number_analysis():
    
    if Player_number>computer_number:
        print(f"\nGuess is Too large ,{Player_number}")

    elif Player_number<computer_number:
        print(f"\nGuess is Too small  ,{Player_number}")
      
    else:
        print(f"you won the game the  Guess Number is {computer_number} ")

print("\n welcome to number guessing game")
print("\nThe number will be in range of 1-100")
difficulty=input("\nEnter the level of difficulty 'easy', 'hard' : ").lower()
if difficulty=='easy':
    total_chance=10
elif difficulty=='hard':
    total_chance=5
else:
    print("Wrong input")    


while total_chance!=0:
    print(f"\nchance remainig ={total_chance}")
    print(f"Previously guessed numbers are ={guessed_numbers}")
    Player_number=int(input("Enter your number:"))
    guessed_numbers.append(Player_number)
    total_chance-=1
    number_analysis()
    if Player_number==computer_number:
        break;
if total_chance==0:
    print('\nYou lost the game')
    print(f"The actual Guess number was {computer_number}")

