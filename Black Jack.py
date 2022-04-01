#Card deck
import random
import time
Userplayer1 = True
UserSum = True

def Deck_of_Cards():
    Card_number = ['Ace','1', '2','3','4','5','6','7','9','10','J','K','Q']
    Card_sign = ['Clubs','Hearts','Spades','Dimond']
    deck = []
    for S in Card_sign:
        for N in Card_number:
            deck.append( N + ' of ' + S )

    return deck
GameDeck = Deck_of_Cards()
#List for the list of cards that is for the player
PlayerCards =[]

#List for the list of cards that is for the player
DelaerCards = []

#Cards value
def Card_Value_(Card_Value):
    Card_Value = Card_Value[:1]
    if Card_Value == 'Q' or Card_Value == 'K' or Card_Value == 'J' or Card_Value == "1":
        return 10
    elif Card_Value == "2":
        return 2
    elif Card_Value == "3":
        return 3
    elif Card_Value == "4":
        return 4
    elif Card_Value == "5":
        return 5
    elif Card_Value == "6":
        return 6
    elif Card_Value == "7":
        return 7
    elif Card_Value == "8":
        return 8
    elif Card_Value == "9":
        return 9



#Ace value
    elif Card_Value == 'A':
        print("\n" + str(Card_Value))
        AceValue = input("Do you want the Ace to be 1 or 11? \nEnter Answer here: ")
        while AceValue != '1' or AceValue != '11':
            if AceValue == '1':
                return 1
            elif AceValue == '11':
                return 11
            else:
                AceValue = input("Do you want the Ace to be 1 or 11? \nEnter Answer here: ")

#start of game ask qusetion
while Userplayer1 == True:
    User = input("Is this your first time playing yes or no:")
#rules for the game
    if User == "yes" or User == "Yes":
        User2 = input("Do you need the rules explained yes or no:")
        if User2 == "yes" or User2 == "Yes":
            print("\nThe Objective of the game Black Jack is for each participant attempts to beat the dealer by "
                  "\ngetting 21 or a count as close to 21 as possible, without going over 21 which is a bust. "
                  "\nYou can add cards to your hand by calling 'hit' or you can choose not to by saying 'stay'. "
                  "\nAt the end if the dealer has less than 16 points, they have to pick up a card. "
                  "\nIf it is 17 or above, they have to stay. If the dealer busts, each player gets x2 their bet. "
                  "\nIf the dealer has a hand larger than all the players, then they get all the bets "
                  "\nbut if any of the players have a higher hand without busting then the person with the highest hand, "
                  "\ngets double their bet and the others who also beat the dealer get their bet back.")
            time.sleep(30)
            print("Ok then lets play the game!!!")
            break

#Game start
        elif User2 == "no" or User2 == "No":
            print("\nOk then lets play the game!!!")
            break

    elif User == "no" or User == "No":
        Play = input("Would you like to play again? Yes or No:")

        if Play == 'yes' or 'Yes':
            print("\nYay!!! Lets play!!")
            break

        elif Play == 'No' or 'no':
            exit()
            break


#start game
print("\nLet's start the Game and deal the cards")

time.sleep(5.5)

#Delears hand
while len(DelaerCards) != 2:
    y = (random.choice(GameDeck))
    GameDeck.remove(y)
    DelaerCards.append(y)
    if len(DelaerCards) == 2:
        print("\nThe delers cards are X and", DelaerCards[1])


#players hand
while len(PlayerCards) != 2:
    x = (random.choice(GameDeck))
    GameDeck.remove(x)
    PlayerCards.append(x)
    if len(PlayerCards) == 2:
        print("\nYour Cards are ", PlayerCards)

#Claculate Dealer hand

Sum = 0
for I in PlayerCards:
    x = Card_Value_(I)
    Sum = Sum + x
    print(Sum)

while UserSum == True:
    if Sum > 21:
        print("You lose")
        break

    elif Sum == 21:

        print("You win")
        break
    #his or stay for player
    elif Sum < 21:
        UserChoice = str(input("Would you like to Hit or Stay?\nAnswer here: "))
        if UserChoice == "Hit" or UserChoice == "hit":
            print("Since you choose hit you will now get a new card")
            time.sleep(2.5)

    #Adding another card to the oridgenal two cards
            x = (random.choice(GameDeck))
            GameDeck.remove(x)
            PlayerCards.append(x)
            if len(PlayerCards) != 1:
                print("Your next card is ", PlayerCards)
                Sum = 0
                for I in PlayerCards:
                    x = Card_Value_(I)
                    Sum = Sum + x
                    print(Sum)

                if Sum == 21:
                    print("Yay you win!!!!")

                elif Sum > 21:
                    print("OOHH!! Sorry but that score it to high.")
                    exit()
        elif UserChoice == "stay" or UserChoice == "Stay":
            print("Time to check for winners")
            break



Som = 0
for L in DelaerCards:
    y = Card_Value_(L)
    Som = Som + y



if Som < 16:
    print("Dealer needs to hit")

    y = (random.choice(GameDeck))
    GameDeck.remove(y)
    DelaerCards.append(y)
    if len(DelaerCards) == 1:
        print("Delers cards are now ", DelaerCards)

elif Som == 21:
    print("Dealer wins")
#Compare score
if Sum < Som:
    print(DelaerCards)
    print("OOOOOHHH!! Sorry the dealer takes this round!! Youb lost against the dealer.")

elif Som < Sum:
    print(DelaerCards)
    print("Yay!! you won against the dealer!! VICTORY!!")

elif Sum == Som:
    print(DelaerCards)
    print("Looks like their is no clear winner. Guess its a draw.")

