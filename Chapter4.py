# Martha Moreno Gonzalez 
# 02/28/2025
import time
import random
import Chapter3

def chapter_4(path, weapon):
    print("Chapter 4: The Warden of The Waters of Fate")
    print("Thor and Snow make it to the end of the path")
    print("They hear a deep voice start to speak it says:")
    print("Morveth: 'None shall pass for i am MORVETH!! The ancient protector of this lake! Only the worthy shall pass!")

    time.sleep(2)
    print("Let the battle begin!")

    if weapon == "Mjölnir":
        print("1. Use **Mjölnir** to strike with lightning! (Huge advantage)")
        print("2. Fight alongside Snow in a powerful team attack!")

    choice = input("Choose 1 or 2: ").strip()

    if choice == "1" and weapon == "Mjölnir":
        print("Thor raises **Mjölnir**, summoning a storm! A bolt of lightning strikes Morveth.")
        print("The warden roars in pain, weakened by the divine power. The battle is easily won!")
    elif choice == "2":
        print("Snow and Thor coordinate their attacks! Snow's agility and Thor’s strength create an unstoppable force.")
        print("Together, they strike down Morveth after a fierce battle!")
    
    print("Boss Defeated")
    chapter_5()
def chapter_5():
    print("Thor and Snow defeated Morveth, the lake awaits them..")
chapter_4(path, weapon)