#Marco Villegas
#6/18/23
import turtle
import gvars2
import random
from random import shuffle
from time import sleep
from random import randint

#Chapter 2
print("\n\n - Chapter 2.py")
print(gvars2.HeroName, 'the amulet is a sign that you should rush to the palace here\
 in Tenrou and have a chat with Queen Luma ruler of dragons. \n')
#Intro to chapter 2

print(gvars2.HeroName, "thinks to themselve,: Wait what? arent you my parents?\
 Parents reply with: No my dear, we are actually loyal servants of the Queen,\
 we were assigned to raise you away in a far land." " We were tasked to watch\
 over you until you received this amulet. \n")

print(gvars2.HeroName, 'you begin to ask questions')
#Questions to parents 

for i in range(3):
    answer3 = input('Who is Queen Luma and what is she? Also I thought you were\
 my parents? Press q1 and then q2: ')
    if answer3 == 'q1':
        print('Queen Luma is a dragon said to rule for over 800 years she is a\
 kind a wonderful ruler. ')
    else:
        print(gvars2.HeroName, 'like we said we were once loyal guardians to Queen\
 Luma but one day she asked us to take you away and to never return to the\
 palace until you received this amulet. \n')
        break
#This will loop until all questions are ask by player

print(gvars2.HeroName, 'learning the shocking news about your birthright you decide\
 to march to the Town of Illyos, which is near the palace. \n')
#Journey to the Palace

print('You see a villager and approach them to get directions ot the Palace. \n')
def villager():
    global npcName
    global response
    responses = ["Sleep and go to the palace the next morning \n", "The palce is\
 quite far, may you be interested staying at a inn? \n", "The palace is a little\
 far up north, would you like to rest before your travels? \n"]
    npcNameChoice = ["Draken", "Scylla", "Wyverne"]
    shuffle(npcNameChoice)
    npcName = npcNameChoice[0]
    print( npcName, ":] Hello, I am ", npcName, ", Queen Luma is a wonderful\
 ruler she watches over us dragon kin all the time, would you like some\
 assitance to get to the palace? \n")
    shuffle(responses)
    answer = input("Press y to continue talking to the villager: ")
    if answer == "y":
        print(npcName, ":] ", responses[0])
    else:
        print(npcName, ":] Goodbye")
    return npcName

npcName = ' '
response= ' '
villager()
#Talking to villager

print(gvars2.HeroName, 'Decides it is best to stay at a inn for the night and travel\
 to the palace gates in the morning. \n')
#This concludes chapter 2

