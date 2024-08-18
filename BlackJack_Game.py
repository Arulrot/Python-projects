import random

game_over=False

while game_over!=True:

    delear_card=[]
    user_card=[]


    def computer_card():
        '''return a random dealer card'''
        cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        card=random.choice(cards)
        return card

    def player_card():
        '''return a random player card'''
        cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        card=random.choice(cards)
        return card

    def adding_cards():
        delear_card.append(computer_card())
        user_card.append(player_card())

    def calculate_score():
        if 11 in user_card and sum(user_card)>=21:
            user_card.remove(11)
            user_card.append(1)


    print(f"The first card of dealer is {delear_card[0]}")
    print(f"Your cards are {user_card} with the total of ")
    game=input("do you want to continue taking card 'y' or 'no':")
    if game=='y':
        continue
    else:
        game_over=True