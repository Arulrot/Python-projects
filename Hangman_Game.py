import random 

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print("\nwelcome to hangman Game")
print("\nGuess the fruit name correctly ")

words= [
    "Mango", "Pineapple", "Strawberry", "Blueberry", "Raspberry",
    "Blackberry", "Watermelon", "Melon", "Peach", "Plum",
    "Apricot", "Cherry", "Kiwi", "Papaya", "Guava",
    "Lychee", "Passionfruit", "Pomegranate", "Coconut", "Fig",
    "Date", "Cranberry", "Mulberry", "Gooseberry", "Starfruit",
    "Dragonfruit", "Jackfruit", "Avocado", "Durian", "Rambutan",
    "Longan", "Persimmon", "Tangerine", "Clementine", "Mandarin",
    "Satsuma", "Navel Orange", "Blood Orange", "Pomelo", "Lime",
    "Lemon", "Grapefruit", "Ugli Fruit", "Quince", "Jujube",
    "Salak", "Mangosteen", "Sapodilla", "Loquat", "Miracle Fruit",
    "Breadfruit", "Bilberry", "Camu Camu", "Elderberry", "Huckleberry",
    "Marionberry", "Olallieberry", "Boysenberry", "Cloudberry", "Serviceberry",
    "Acerola", "Chokeberry", "Medlar", "Sea Buckthorn", "Nance",
    "Jabuticaba", "Santol", "Cherimoya", "Soursop", "Custard Apple",
    "Rose Apple", "Ambarella", "Hog Plum", "Feijoa", "Calamondin",
    "Buddha's Hand", "Finger Lime", "Calabash", "Pawpaw", "Surinam Cherry",
    "Cupuacu", "Cacao", "Ceylon Gooseberry", "Langsat", "Langka",
    "Atemoya", "Pulasan", "White Sapote", "Mamey Sapote", "Sapote",
    "Sugar Apple", "Noni", "Kumquat", "Tamarillo", "Bacaba",
    "Barbados Cherry", "Bael", "Bignay", "Caimito", "Canistel"
]


selected_word=random.choice(words)
lenght_of_selectedword=len(selected_word)
for i in range(lenght_of_selectedword):
    print("_",end=' ')

print("\nTotal life you have is: 6")
guess=[] 
chance=0

Game_over=False

while not Game_over:
    
    display=''
    guess_word=input("\nEnter a letter:").lower()
    for char in selected_word:

        if char==guess_word:
            display+=char
            guess.append(guess_word)
            
        elif char in guess:
            display+=char
           
        else:
            display+='_'
    if guess_word not in selected_word:
        chance+=1        
        
            
    print("\nRemaining chance is:",6-chance)
    print("\n",display)
    print(HANGMANPICS[chance])
    if chance==6:
      print("\nGame over")
      print("\nThe word is:",selected_word)
      print("\nYou lose")
      Game_over=True

    if '_' not in display:
        Game_over=True
        print("\nyou won ")
