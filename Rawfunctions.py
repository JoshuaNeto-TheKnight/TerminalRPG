import random
import Defensefunctions

def powerdice():
    Stats = []
    ChoiceFinale = "N"
    Choice = 0
    while ChoiceFinale == "N":
        pity = 0
        while True:
            print("Tell me, do you often find yourself as a strong-willed person with a thick skinned tolerance?")
            print("[Y]es [N]o")
            HP = 0
            Choice = input()
            if Choice == "Y":
                HP = 60
                break
            elif Choice == "N":
                HP = 50
                pity += 1
                break
            else:
                print("Let us try this again.")
        while True:
            print("Are you a brave person that will soldier on regardless of your weaknesses?")
            print("[Y]es [N]o")
            DEF = 0
            Choice = input()
            if Choice == "Y":
                DEF = 2
                break
            elif Choice == "N":
                DEF = 1
                pity += 1
                break
            else:
                print("Let us try this again.")
        while True:
            print("Do you find yourself as a righteous one?")
            print("[Y]es [N]o")
            PWR = 0
            Choice = input()
            if Choice == "Y":
                PWR = 5
                break
            elif Choice == "N":
                PWR = 3
                pity += 1
                break
            else:
                print("Let us try this again.")
        while True:        
            print("Are you a resilient person? Being more stubborn than you can backup with?")
            print("[Y]es [N]o")
            DEF = 0
            Choice = input()
            if Choice == "Y":
                DEF = 2
                break
            elif Choice == "N":
                DEF = 1
                pity += 1
                break
            else:
                print("Let us try this again.")
        print("Now, for an odd question...")
        while True:
            print("Which of these dinning utensils is your go-to?")
            print("[S]poon [F]ork [K]nife")
            Choice = input()
            if Choice == "S":
                weaknesses = [0.5, 1,0, 2.0]
                break
            elif Choice == 'F':
                weaknesses = [2.0, 0.5, 1.0]
                break
            elif Choice == 'K':
                weaknesses = [1.0, 2.0, 0.5]
                break 
            else:
                print('Respond within the options asked...')
        print('Let me throw another oddball...')
        defensive
        while True:
            print('What type of action fits with your person?')
            print('[P]assive [N]eutral [A]ctive')
            Choice = input()
            if Choice == 'P':
                defensive = Defensefunctions.Guard
                break
            elif Choice == 'N':
                defensive = Defensefunctions.Counter
                break
            elif Choice == 'A':
                defensive = Defensefunctions.Evade
                break
            else:
                print('Please, answer with the options in mind.')
        print('Your form takes a new shape ...')
        Stats = [HP, DEF, PWR, defensive,weaknesses]

    return Stats

def statuscheck(H, P, D):
    print(H)
    print(P)
    print(D)

def welcome():
    print("Welcome to The City...")
    print("Where you Face The Fear, and Build The Future...?")
    print("Argh, thats unimportant. Now, what's your name, fresh blood?")
    name = input("Insert your nickname: ")
    print("Ah, right... you seem familiar with these streets, right?")
    print("[Y]es.", "[N]o.")
    while True:
        choice = input()
        if choice == "Y":
            print("Alright then, good luck out there, ya will need it...")
            break
        elif choice == "N":
            print("You have a screw loose? Heh, well...")
            print("Here, take this then.")
            break
        else:
            print("Speak with your brain, not ya tounge!")
    print(f'As a last advice: death will be your only sweet release, {name}...')
    return name


def pathchoices(choice1, choice2):
    print("/With that chit-chat over with, what path you will take?/")
    print("[L]eft" , "[R]ight")
    while True:
        choice = input()
        if choice == "L":
            path = choice1
            break
        elif choice == "R":
            path = choice2
            break

def dmgform(PWR, AGI, EDEF):
    AGI = random.randint(0, AGI)
    DMG = (PWR * (1 + AGI)) - EDEF
    DMG = int(DMG)
    return DMG
    

def thugfight(PlayerName, YHP, YPW, YDF, EHP, EPW, EDF, EnemyName):
    EnemyHP = EHP
    EnemyPOWER = EPW
    EnemyDEFENSE = EDF
    DMG = dmgform(YPW, YDF, EDF)
    print("/Battle Start!/")
    while EHP > 0:
        print(EnemyName,"health:",EHP)
        print(f'HP: {YHP}, PWR: {YPW}, DEF: {YDF}')
        print(f"/How should {PlayerName} engage?/")
        print("[A]ttack", "[D]efend")
        while True:
            action = input()
            if action == "A":
                EHP = EHP - DMG
                break
            else:
                print("Focus!")
        enemychoice = random.randrange(1,3)
        if enemychoice == 1:
            print("He produces a knife from his pocket and swings at you!")
            YHP = YHP - EPW
        elif enemychoice == 2:
            print("The thug rests for a bit")
            EHP = EHP + EDF
        elif enemychoice == 3:
            print("The thug continues to glare at you")
            
    print("You won!")
    return YHP        

def nestencounter():
    return

def thugencounter(name, H, P, D):
    print("/You walk out of the Nest, with only gray-smoke buildings and a heavy mist above you drowing your view of the sky/")
    print("/Then suddenly, you feel footsteps behind your back/")
    print("/You swiftly turn to the direction of the sound/")
    print("/There is a lone, shady figure in the road, he seems dangerous.../")
    print("/Should you: [F]ight?/")
    YH, YP, YD = H, P , D
    while True:
        choice = input()
        if choice == "F":
            path = thugfight(name,YH, YP, YD, 20, 1, 2, "Thug")
            return
        if choice != "F":
            print("Try again")
    return H