#Marco Villegas
#6/18/23
import turtle
import gvars2
import random
from random import shuffle
from time import sleep
from random import randint


#Chapter 3
print("\n\n - Chapter 3.py")
print(gvars2.HeroName, 'with high spirits is delighted to learn of their past and\
 discover why you were sent away at a young age by Queen Luma, as you make your\
 way in to the Palace. \n')
#Intro to Chapter 3



print('Palace Guards: Who are you?, I am', gvars2.HeroName,'!!! and I wish\
 to see Queen Luma', 'Palace Guards: Well.. You dont seem suspicious you\
 may enter. \n')

print('Queen Luma: Is tha-- thats--', gvars2.HeroName,'!!! Are you mm- my child? \n')
print('With a warm embrace you hug Queen Luma your mother; meanwhile you notice\
 a similar completed amulet around Queen Luma neck!? and decide to show your broken\
 amulet and ask some questions. \n')
#Entering palace and meeting Queen Luma




for i in range(3):
    answer4 = input('Why was I sent to a small village and raised there?\
 Wow that is a preety amulet you have there it looks like mine, why is that?\
 Press q1 and then q2: ')
    if answer4 == 'q1':
        print('You see', gvars2.HeroName, 'I had to send you away because I was being\
 targeted for an assasination and I didnt want you in harms way.\n')
    else:
        print(gvars2.HeroName, 'this amulet gives power to us dragon kin. While we may\
 have some power as dragons this amulet is essential to unlocking our potential\
 and be able to achive great feats. \n')
        break
#This will loop until all questions are ask by player




print('After being content with the answers given you decide to have dinner and\
 go and explore the Palace talk with the royal guards and maybe see the Palace\
 Gardens too. \n')
#Exploring the Palace



print('You see a royal guard and approach them. \n')
def guard():
    global npcName
    global response
    responses = ["Things have been different around here \n", "Queen Luma has\
 been wanting to expand her territory and we do not know why? \n", "The palace\
 has been chaotic since you arrived a lot of plans are being made! \n"]
    npcNameChoice = ["Draco:", "Wrather:", "Mynerva:"]
    shuffle(npcNameChoice)
    npcName = npcNameChoice[0]
    print(npcName, "ahhh! you must be", gvars2.HeroName,", Queen Luma has talked so\
 much about you. You ask: How is Queen Luma ruling over Tenrou?", npcName,"\
 Well actually she has been driven sort of mad, she plans to go to\
 war with the neighboring kingdoms. \n")
    shuffle(responses)
    answer = input("Press y to continue talking to the guards: ")
    if answer == "y":
        print(npcName, ":", responses[0])
    else:
        print(npcName, ":] Goodbye")
    return npcName

npcName = ' '
response= ' '
guard()
#Talking to guards




print(gvars2.HeroName, 'decides to investigate as you make your way to the Palace\
 Gardens. \n')

print('A shadow figure appears before you. They are wearing a dark cloth covering\
 their face. They attack with Abominations! and shadow attacks. You are left wiht\
 no choice but to used the power of the amulet and transform to a white mystical\
 dragon and fight. \n')
#Exploring the Gardens




def fight():
    outcomes = ['Win!', 'Attacking with Light breath attack', 'Attacking with\
 light attacks', 'Attacking with dragon claws and tail']
    print('\nIt looks like you are ready to fight... Let\'s see what the\
 outcome is..')
    sleep(0.5) #waiting for half a second
    return outcomes[randint(0,2)] #genrates a random number between 0-2

key = False

while key == False:
    result = fight()
    print(result)
    if result == 'Win!':
        key = True
        print('You managed to defeat the masked figure, they scurry off\
 then a similar white glow appears... \n')
#Fighting scene with masked figure 



print('The Goddess appears before you: Hello young one, I came only to warn\
 you of the dangers ahead. If you stay here you will be hurt or worse killed!\
 I implore you to please run away and train with the power of the amulet! \n')

for i in range(3):
    answer5 = input('Will you run away to train?: Press y or n: ')
    if answer5 == 'n':
        print(gvars2.HeroName, 'I implore you to please reconsider, if you go\
 back I wont be thre to protect you. You can be killed! Please make the right\
 choice. (Press y to continue story) \n')
    else:
        print('I am glad you heard my warning', gvars2.HeroName, 'I think if you seek\
 refuge in the woods and or mountians, of the village you use to live in. I bet\
 there you can hone your skills and power there. \n')
        break
#This will loop until player makes the right choice



print(gvars2.HeroName, 'decides to take a long trip back home to their village\
 although you are scared and confused as to why you must hone your skills.\
 Eitheir way you think that trusting the Goddess is important since she has\
 saved your life before. You say goodbye not knowing you wont see this palace\
 for years to come... \n')
#This concludes chapter 3

