def light():
    print("You find yourself in a void so dark, it burns your eyes, then, almost in an instant, a spark starts talking to you...")
    print("I will be your guiding light, even in your lowest of lows, I shall shelter you.")
    print("Do you understand?")
    print("-Answer the prompts with any highlighted letters", "[Y]es", "[N]o")
    choice = input()
    print("Good... Now... Tell about yourself:")
def powerdice():
    HP = 50
    PWR = 2
    DEF = 1
    print("Are you a strong person?")
    print("[Y]es" , "[N]o")
    while True:
        choice = input()
        if choice == "Y":
            PWR = PWR + 1
            print("You feel more powerful...")
            break
        elif choice == "N":
            HP = HP + 5
            print("You feel more healthy...")
            break
        else:
            print("I didn't hear it right... Could you reinstate it?")
    print("Do you think of yourself as a fast person?")
    print("[Y]es" , "[N]o")
    while True:
        choice = input()
        if choice == "Y":
            DEF = DEF + 1
            print("You feel more dexterous")
            break
        elif choice == "N":
            HP = HP + 5
            print("You feel more healthy")
            break
        else:
            print("I didn't hear it right... Could you reinstate it?")
    print("Are you a persistant person?")
    print("[Y]es" , "[N]o")
    while True:
        choice = input()
        if choice == "Y":
            DEF = DEF + 1
            print("You feel more dexterous")
            break
        elif choice == "N":
            HP = HP + 5
            print("You feel more healthy")
            break
        else:
            print("I didn't hear it right... Could you reinstate it?")
                
    return HP, PWR, DEF
    
def statuscheck(H, P, D):
    print(H)
    print(P)
    print(D)

def welcome():
    print("Welcome to The City.")
    print("Where you Face The Fear, and Build The Future.")
    print("Now, what's your name, fresh blood?")
    name = input("Insert your nickname: ")
    print("Ah, you seem unfamiliar with these streets, right?")
    print("[Y]es.", "[N]o.")
    while True:
        choice = input()
        if choice == "Y":
            print("Alright then, good luck out there, ya will need it...")
            break
        elif choice == "N":
            print("You have a screw loose? Heh, well...")
            break
        else:
            print("Speak with your brain, not ya tounge!")
    print(f'As a last advice: death will be your only sweet release, {name}...')
    return name


def pathchoices():
    print("With that chit-chat over with, what path you will take?")
    print("[B]ackstreets" , "[N]est")
    while True:
        choice = input()
        if choice == "B":
            Backstreets = thugencounter()
            break
        elif choice == "N":
            Nest = nestencounter()
            break


def thugencounter():
    print("You walk out of the Nest, with only gray-smoke buildings and a heavy mist above you drowing your view of the sky.")
    print("Then suddenly, you feel footsteps on your ")
