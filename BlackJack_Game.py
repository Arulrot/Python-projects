import random

user_cards=[]
computer_cards=[]

def dealer_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,]
    card=random.choice(cards)
    computer_cards.append(card) 

def player_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,]
    card=random.choice(cards)
    user_cards.append(card)

def calculate_score():
    if sum(user_cards)==21 and len(user_cards)==2:
        return 0
    
    if 11 in user_cards and sum(user_cards)==21:
        user_cards.remove(11)
        user_cards.append(1)