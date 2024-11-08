#create an empty list to hold all cards
cards = []

#create two cards
card1 = ("Jack", "Diamond", "Red")
card2 = ("Ace", "Spade", "Black")

#add the two cards to the list of cards
cards.append(card1)
cards.append(card2)

#show the list
print(cards)

# first_card = cards[0]
# print(first_card[0])
# print(cards[0][0])

#loop through all cards
for card in cards:
    print(card)
    #you can use join if you just want the info of the cards without the tuples
    #print(",".join(card))



