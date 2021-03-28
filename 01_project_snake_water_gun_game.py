# WAP to make Snake, Water and Gun game !

import random                                           # imports random module so that comp move is not baised instead random and fair


def gameWin(comp, you):                                 # defining function where it can do operations on two input
    
    if comp == 's':                                     # conditions for game
        if comp == you:
            print("Tie!")
        elif you == 'w':
            print("Comp wins!")
        elif you == 'g':
            print("You wins!")

    if comp == 'w':
        if comp == you:
            print("Tie!")
        elif you == 'g':
            print("Comp wins!")
        elif you == 's':
            print("You wins!")

    if comp == 'g':
        if comp == you:
            print("Tie!")
        elif you == 's':
            print("Comp wins!")
        elif you == 'w':
            print("You wins!")


print("Comp's Turn: Snake(s), Water(w) and Gun(g)")     # for fair game comp's move will not be visible, until your move
randNo = random.randint(1, 3)                           # randomizing the comp's move
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s), Water(w) and Gun(g): ")

gameWin(comp, you)                                      # calling function

print(f"\nComp's move: {comp}")
print(f"Your move: {you}")