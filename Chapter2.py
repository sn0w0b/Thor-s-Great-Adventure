# Martha Moreno Gonzalez 
# 02/28/2025

import time
import random

def chapter_2_intro():
    print("Chapter 2: Welcome to the pub!")
    
    time.sleep(5)
    print("Thor and the girl make aquantinces.")
    print("She leads him to a nearby tavern where the adventure continues...")
    print("At the pub, Thor learns about an enchanted, beautiful trail that leads to a mystical lake.")
    print("According to legend, the lake can show visions of the future to those who seek its wisdom.")
    print("Thor also learns that his new friend’s name is Snow. She, like Thor, is always looking for adventure.")

def chapter_2_pt_2():
    time.sleep(2)
    print("Thor and Snow decide to embark on a journey to this mysterious lake.")
    print("How would you like to prepare for the journey?")
    print("1. Prepare thoroughly for the journey by youself (Start Chapter 3 well-prepared)")
    print("2. Sleep in and delay the trip (Start Chapter 3 at a disadvantage)")
    print("3. Talk with Snow and plan carefully (Start Chapter 3 with an great advantage)")

    choice = input("Choose 1, 2, or 3: ").strip()
    
    if choice == "1":
        print("Thor gathers supplies and make sure he is well-equipped before leaving.")
        chapter_3("normal")
    elif choice == "2":
        print("Thor decides to sleep in. Very unprepared and hungry.")
        chapter_3("disadvantage")
    elif choice == "3":
        print("Thor and Snow spend time discussing the journey and carefully planning their route.")
        print("Their preparation gives them an advantage when they start the journey!")
        print("Thor and Snow's bond grew a bit more.")
        chapter_3("advantage")
    else:
        print("Invalid choice. Try again.")
        chapter_2_pt_2()
def chapter_3():
    print("Let the adventure really begin now!!")
chapter_2_intro()