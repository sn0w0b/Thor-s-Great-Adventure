#Martha Moreno Gonzalez 
#02/28/2025
import time
import random

def start_game():
    print("Welcome to your adventure!")
    ready = input("Are you ready for it to begin? (Yes/No) ").strip().lower()
    if ready == "yes":
        chapter_1_pt_1()
    else: 
        print("Come back when you are ready.")
        exit()
def chapter_1_pt_1():
    time.sleep(2)
    print("It's morning, Thor wakes up in a torn-down chapel. Just down the road is a kingdom.")
    print("Thor: It's time to go exploring!")
    print("1. Walk towards the kingdom")
    print("2. Stay in the chapel a bit longer")

    choice = input("Choose 1 or 2").strip()
    
    if choice == "1":
        print("Thor begins to walk towards the kingdom, what adventure will be awaiting him?")
        chapter_1_pt_2
    elif choice =="2":
        print("Thor decides to rest up a bit longer")
        time.sleep(5)
        chapter_1_pt_1()
    else:
        print("Invalid choice. Try again")
        chapter_1_pt_1()
def chapter_1_pt_2():
    time.sleep(2)
    print("Thor walks towards the kingdom,")
    print("The kingdom seems to be busy and lively, filled vendors and people socializing.")
    print("You are walking and you accidentally bump into a girl. She drops everything!")
    
    reactions = ["She apologizes.", "She looks annoyed.", "She says nothing."]
    print(random.choice(reactions))

    print("What do you do?")
    print("1. help her pick up her things")
    print("2. apologize profusely")
    print("3. ask for directions, invite her to a drink as an apology")

    choice = input("Choose 1, 2, or 3").strip()
    
    if choice == "1":
        print("Thor kneels down and helps her pick up her things. She smiles and thanks him warmly.")
    elif choice =="2":
        print("Thor keeps apologizing, feeling awkward. The girl sighs and picks up her own things.")
    elif choice == "3":
        print(" 'Im so sorry for that, let me buy you a drink as an apology!' ")
        chapter_2()
    else:
        print("Invalid choice. Try again")
        chapter_1_pt_2()
def chapter_2():
    print("Welcome to the pub, choose wisely....")

start_game()





