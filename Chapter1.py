#Marco Villegas
#6/18/23

#Chapter 1
print("\n\n - Chapter 1.py")
import turtle
import gvars2
import random
from random import shuffle
from time import sleep
from random import randint



print('It was a bright morning, in the year X971, winds so smooth you felt them\
 guide you as you made your way through the woods and find your home \n')
#Intro to story 

print(gvars2.HeroName, 'thinks to themselve: It is such a beautiful day, wait what\
 is that? \n')
      
def monster():
    global response
    responses = ["What is that thing?", "AHH! look at the size of the monster\
 ", "What is that ugly thing?"]
    print('A huge monster appears, it is called a Abominations known in\
 Tenrou. These abominations have a large body like a bear, a mouth that spreads\
 open his whole face to eat its prey, and sharp venomous teeth. \n')
    print(random.choice(responses))
    ans = input("Press y to sneak closer to it or n to observe: ")
    while ans != "y":
        print("Let me get closer... the abomination is looking for you\
 frantically", gvars2.HeroName, "thinks: I should sneak past it...")
        ans = input("Press y to sneak closer to it or n to observe: ")
    print("Oh no it spotted me!")

response = ' '
monster()
#Abomination encounter


for i in range(3):
    answer1 = input('Do you want to run away(y) or hide(n)? y or n: ')
    if answer1 == 'n':
        print('you ran away and hid for a while but... the abomination\
 found you \n')
    else:
        print(gvars2.HeroName, 'decided to take a shortcut but you happened to trip\
 just when all hope is lost a mysterious figure apppears in a bright white\
 light \n')
        break
#This will loop until correct answer is given by player


print('Do not fret young child... take this amulet and vanquish the abomination\
 before you. \n')
#Goddess appears to the rescue


for i in range(3):
    answer2 = input('Do you take the half broken amulet from mysterious\
 person y or n: ')
    if answer2 == 'n':
        print(gvars2.HeroName, "begins to run away and hide but... the Goddess\
 appears again and demands you take the amulet! \n")
    else:
        print(gvars2.HeroName, "Used the broken amulet and defeated the abomination\
 you begin to rush home. \n")
        break 
#Defeats abomination and is heading to parents

print('Parents: My what happened?', gvars2.HeroName, 'You are hurt and oooh--- is that th- the-\
 amulet?', 'My dear child you must sit, there is something you should know.')
#This concludes chapter 1
