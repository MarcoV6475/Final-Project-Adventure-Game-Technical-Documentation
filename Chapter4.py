#Marco Villegas
#6/18/23
import turtle
import gvars2
import random
from random import shuffle
from time import sleep
from random import randint


#Chapter 4
print("\n\n - Chapter 4.py")
print('The year is X976 you have been training your, mind, body, and light magical\
 attacks; also you find out new information about Queen Luma’s plans to go to war\
 with the neighboring Kingdoms \n')

print(gvars2.HeroName, 'makes their way back to the palace of Tenrou to\
 confront Queen Luma. \n')
#Heading back to the Palace 



print('It has been 5 years of constant training', gvars2.HeroName, 'wraps on\
 a large cloth concealing them from the villagers near the Palace.\
 You have made your way through the town and approach the castle gates. \n')
for i in range(3):
    answer6 = input('Do I sneak in the Palace(y) or begin my attacks now?(n)\
 Press y or n: ')
    if answer6 == 'n':
        print('You begin to take on the guards to enter the Palace but there\
 is too many soldiers, you decide to flee and try again another day. \n')
        print("Next day... \n")
    else:
        print('You skilfully make your way into the Palace gates, you attack\
 the guards slowly and carefully until you reach the throne room. \n')
        break
#Brekaing into the Palace 



print(gvars2.HeroName, 'you find Queen Luma alone in the throne room and she seems\
 to be looking at a map most likely planning to attack the kingdoms soon! \n')

print('Queen Luma hides the plans and runs toward you.', 'Thena I am sooo glad\
 your\'e okay, I thought one of the nearby Kingdoms had kidnapped you, are you\
 alright?', gvars2.HeroName,': pushes Queen Luma away and demands to know why is she\
 planning to go to war; this can harm the villagers and possibly ruin the Kingdom\
 of Tenrou.', 'Queen Luma responds: How DARE you imply that you know what is right\
 for the dragons of Tenrou, you ran away, never lending a hand!!!! Rage consumes\
 her and transforms into her dragon form with scales shining with radiant power\
 ! \n')

def fight():
    outcomes = ['Attack: Bright Light', 'Attack: Light Breath','Attack:\
 Magical Rain of Light', 'Attack: Light Dragon Fangs', 'Attack: Light\
 Dragon Slash']
    print('\nIt looks like you are ready to fight... Let\'s see what the\
 outcome is..')
    sleep(0.5) #waiting for half a second
    return outcomes[randint(0,2)] #genrates a random number between 0-2

key = False

while key == False:
    result = fight()
    print(result)
    if result == 'Attack: Bright Light':
        key = True
        print('You managed to, muster up your remaining strength and unleash\
 a bright light which revealed a dark secret.... \n')
#Fighting scene with Queen Luma



print('The Queen Luma before you is infact the same masked foe you fought 5\
 years ago!? Weak and confused of this knowledge you decide to give up but then\
 .... the Goddess appears to help you in your final moments! \n')

print(gvars2.HeroName, 'I know you think this is over but it is NOT! You can do this!\
 Allow me to use my divine powers and help you defeat this wicked foe. \n')

for i in range(3):
    answer7 = input('Will you allow the Goddess divine power to aid you\
 : Press y or n: ')
    if answer7 == 'n':
        print(gvars2.HeroName, 'sadly declines her divine power and is\
 drawn on to a fight of her life. Draining most of your power', gvars2.HeroName, 'decides\
 it is best to run away and heal... as your fightint the Goddess appears...\
 (Press y to continue) \n')
    else:
        print(gvars2.HeroName, 'along with the power of the Goddess unleash a divine\
 holy trinity attack as a last ditch effort to stop this foe. \n')
        break
#This will loop until player unleashes divine holy trinity attack




def fight2():
    outcomes = ['Attack: Divine Holy Trinity', 'Attack: Light\
 Breath', 'Attack: Magical Rain of Light', 'Attack: Light Dragon Slash', 'Attack:\
 Light Dragon Fangs']
    print('\nIt looks like you are ready to fight... Let\'s see what the\
 outcome is..')
    sleep(0.5) #waiting for half a second
    return outcomes[randint(0,2)] #genrates a random number between 0-2

key = False

while key == False:
    result = fight2()
    print(result)
    if result == 'Attack: Divine Holy Trinity':
        key = True
        print(gvars2.HeroName, 'along with the Goddess divine power defeated the\
 wicked foe in front of them. \n')
#Final attack againts the imposter Queen Luma

        

print(gvars2.HeroName, 'along with the Goddess, run towards the imposter Queen Luma;\
 and can now, after these 5 long years, know the truth... \n')
#This concludes chapter 4

