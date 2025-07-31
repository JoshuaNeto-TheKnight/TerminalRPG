import disfunction
import random
print("/You find yourself in a void so dark, it burns your eyes, then, almost in an instant, a spark starts talking to you.../")
print("I will be your guiding light, even in your lowest of lows, I shall shelter you.")
print("Do you understand?")
print("/Answer the prompts with any highlighted letters/", "[Y]es", "[N]o")
choice = input()
while True:
    if choice == "Y":
        print("Good... Now... Tell about yourself:")
    elif choice == "N":
        print("Good to know... Now, to your preferences...")
    else:
        print("Hm? Sorry, be clearer next time, speaking of which...")
YourStats = disfunction.powerdice()

name = disfunction.welcome()

YourStats = disfunction.pathchoices(disfunction.thugencounter(name, MAXHP, INIPWR, INIDEF), disfunction.nestencounter())