import random

#suffle with Fisher–Yates shuffle
#https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
def shuffle(cards):
    for i in range(len(cards)-1,0,-1):
        j = random.randrange(0,i+1)

        temp = cards[i]
        cards[i] = cards[j]
        cards[j] = temp


#create an empty list to hold all cards
cards = []

suits = ("Diamond", "Spade", "Club", "Heart")

#go through all ranks for cards
for num in range(2,15):
    if num == 11:
        rank = "Jack"
    elif num == 12:
        rank = "Queen"
    elif num == 13:
        rank = "King"
    elif num == 14:
        rank = "Ace"
    else:
        rank = str(num)
    
    #we need to create 4 suits for every cards
    for suit in suits:
        color = "Black"
        if suit in ["Diamond", "Heart"]:
            color = "Red"
        
        #create the card
        card = (rank, suit, color)

        #add the card to the list of cards
        cards.append(card)


#show the total number of cards
print(f"We have {len(cards)} cards")
print()
#loop through all card and print them
print("Here are the cards:")
for card in cards:
    print(card)

print("Shuffling the cards")
#show the cards after they have been shuffled
shuffle(cards)
print("Here are the cards:")
for card in cards:
    print(card)