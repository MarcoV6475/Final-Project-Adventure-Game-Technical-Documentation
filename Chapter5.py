#Marco Villegas
#6/18/23
import turtle
import gvars2
import random
from random import shuffle
from time import sleep
from random import randint



def queen():
    global response
    responses = ["I- I- I can\'t belive it mother?", "You\'re not lying rigth?\
 mother is that you?", "Mo- Mother... is that you? I have you back in my life"]
    print('The goddess grabs your hand and tells you: ', gvars2.HeroName, 'I am in\
 fact...the late Queen Luma... I have been with you since the start as this\
 Goddess. \n')
    print(random.choice(responses))
    save = input("Press y to use your divine power or n to not use them: ")
    while save != "n" and save != "y":
        save = input("Error, please enter y or n: ")
    if save == "n":    
        print("I should at least try to save you, mother... (Press y to save\
 her)")
    else:
        #save = input("Press y to use your divine power or n to not use them: ")
        print(gvars2.HeroName,'grabs ahold of the amulet and tightly grasp them\
 towards your heart and you start wishing and hoping for your mothers\
 return...\n')
    



def start():
#Chapter 5
    print("\n\n - Chapter 5.py")
    print('A scene from the past plays: The masked figure that stood before you\
 was once a young dragon with no family; Queen Luma decided to raise her as her\
 daughter, known as Dracona. Throughout the years Dracona became accustomed to\
 her way of living and decided to rule the kingdom of Tenrou for herself. Dracona\
 planned an assasination on Queen Luma and took an illusion form of her thus\
 assuming ruler of Tenrou, with the Queen\'s Face. \n')

    print(gvars2.HeroName, 'realizes that your biological mother is dead and\
 that Dracona has been mascarading as the late Queen.', gvars2.HeroName,'*falls\
 to the ground* and cries out in agony.  \n')
#Distraught tramtic scene takes place/Intro




    print(gvars2.HeroName, 'angered by this knowledge goes to Dracona, your sister;\
 and you notice the amulet around her neck. As you get close the illusion\
 fades away and you see that the amulet around her neck is the other half of\
 your amulet! \n')
    
    answer8 = input('Do you take the amulet from you sister, Dracona?\
 Press y or n: ')
    while answer8 != "n" and answer8 != "y":
        answer8 = input("Error, please enter y or n: ")
    if answer8 == 'n':
        print(gvars2.HeroName, 'decides it is best to take revenge and kill Dracona\
 avenging your mother. This makes the Goddess fade away as she noticed you\
 have clinged to the darkness... In time you become heir to the Kingdom\
 and rule with hatred in your heart; thus dooming the Dragon Kingdom of\
 Tenrou. (BAD ENDING) \n')
        gvars2.gameover()
    else:
        print(gvars2.HeroName, 'decides to take the amulet away from Dracona... \n')
         
#Bad Ending/Good ending seperation 





    response = ''  
    queen()

    print('All of the sudden, a fog seeps out of the amulet and a bright glimmering\
 light shines from the amulet. By combining the amulets together you have\
 allowed Queen Luma’s spirit to manifest to the real world. Dracona\'s body\
 starts to fade... \n')
#Saving the REAL Queen Luma


    for i in range (3):
        answer9 = input('Do you save Dracona, your sister? Press y or n: ')
        if answer9 == 'n':
            print(gvars2.HeroName, 'witnesses as Dracona\'s body start to fade away\
 never to be seen again (Choose y for Happy Ending) \n')
        else:
            print(gvars2.HeroName, 'rushes to Dracona\'s side and with the power of\
 Queen Luma\'s divine power you save Dracona\'s life and stop her from fading\
 away.\n')
            break
#Deciding Draconas fate




    print('The year is now, X977, you have claimed throne of Tenrou. In the past\
 year you have established a healthy relationship with Dracona who is now working\
 as guardian of Tenrou.', gvars2.HeroName, 'has gained the ability to use divine\
 powers; and with your new divine powers you can, manifest Queen Luma and\
 ask for her guidance when needed. The three of you rule over the Dragon\
 Kigndom of Tenrou with love and prosperity. (HAPPY ENDING! <3) \n')
#This concludes chapter 5 Happy Ending!

    print('The Game has Ended! Congratulations on beating: The Divine Dragon Game!')
    exit()
