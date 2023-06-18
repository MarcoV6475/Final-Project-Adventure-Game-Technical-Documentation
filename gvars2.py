#Marco Villegas
#6/18/23
global HeroName
HeroName = "MC"

def gameover():
    print(HeroName, "you have gotten th BAD ENDING! route...")
    choice = input("Do you want to re-start the chapter?: R to retry\
 , Q to quit: ")
    while choice != "R" and choice != "Q":
        choice = input("Please input Q or R: ")
    if choice == "R":
        import Chapter5
        Chapter5.start()
    else:
        exit()
#gameover()
