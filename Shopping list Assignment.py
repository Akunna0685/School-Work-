#Shopping List
#Introduction
print("Your shopping list has 6 Items they are:")
UserCostom = True
UserCostom1 = True
#Shoppinglist content
ShoppingList = ["Milk", "Chocolate", "Bananas", "Onions", "Chicken", "Spagettie"]
print(ShoppingList)
#Ask if they want to add something with input
UserChoice = input("Would you like to add any Items? \nList them here:")
#List the list with the added item
ShoppingList.append(UserChoice)
print(ShoppingList)


while UserCostom == True:
    # Double Check if anything should be added
    UserAddMaybe = input("Do you want to Add anything else? Press Y if you do. Press N if not\nAnswer here:")

    #If Y list the items in here with input

    if UserAddMaybe == "Y":
        Userchoice = input("List them here:")
        ShoppingList.append(Userchoice)

#if no items to add give an option of removing

    elif UserAddMaybe == "N":
        Userchoice2 = input("Would you like to remove something then? \nList them here:")
        ShoppingList.remove(Userchoice2)
        break

while UserCostom1 == True:
    #final Check if they wast to add or remove something

    LastChance = input("Would you like to add or remove anything else. \nPress A to add. \nPress R to remove \nPress C to see your final list \nEnter awnser here:")

    #add items for last time

    if LastChance == "A":
        Userchoic3 = input("List the items you want to add here:")
        ShoppingList.append(Userchoic3)
    #remove items for last time

    elif LastChance == "R":
        Userchoice4 = input("List the items you want to remove here:")
        ShoppingList.remove(Userchoice4)
#cancel and see final list

    elif LastChance == "C":
        break

print("This is your final Shopping List " + str(ShoppingList))
