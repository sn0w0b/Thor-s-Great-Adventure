# Martha Moreno Gonzalez 
# 02/28/2025

import time
import random
import Chapter2

def chapter_3(status):
    time.sleep(2)
    print("Chapter 3: The Journey to the Enchanted Lake Begins...")
    
    if status == "advantage":
        print("Snow gives Thor a lantern with a strange glow.")
        print("Snow: 'This lantern has a bit of luck in it. It might help guide our way.'")
    elif status == "disadvantage":
        print("Because of their late start, the sun is already high, and the journey feels rushed.")
    else:
        print("Thor and Snow set off early in the morning, ready for the adventure ahead.")
     
    time.slee(2)
    print("Thor and Snow walk a long the road.")
    print("The trail goes deeper and deeper into the forest.")
    print("They are then met at a fork in the road. They have to make a decison..")
    print("To go down the dark path (cuts the trip in half)") 
    print("Or the lit up path that makes the trip longer (villan free as well)")

    if status == "advantage":
        print("The lantern that Snow gave you flickers brighter towards the dark path, its seems to be filled with somesort of magic.")
        print("Snow: 'It seems the lantern is showing us the path. Maybe we should take the dark path.'")
        
        choice = input("Which path do you choose? (1. Dark Path or 2. Lit Path): ").strip()
        if choice == "1":
            print("Thor and Snow venture to the dark path. Ever so cautiously.")
            dark_path(status)
        elif choice == "2":
             print("Thor and Snow take the safer, longer path, avoiding danger but losing time.")
             lit_path(status)
def dark_path(status):
    time.sleep(2)
    print("The darkness surrounds them as they venture deeper into the shortcut.")
    
    if status == "advantage":
        print("The lantern suddenly flares up, revealing a hidden pitfall just ahead!")
        print("Thanks to Snow’s lantern, they avoid the danger and move ahead unharmed.")
        print("As Thor steps forward, his foot hits something metallic... He bends down and lifts it up.")
        print("It's a hammer, heavy yet perfectly balanced. An inscription reads:")
        print("'Whosoever holds this hammer, if they be worthy, shall possess the power of Thor.'")
        print("This is **Mjölnir**, the legendary hammer!")
        chapter_4("dark", "Mjölnir")
    else:
        print("The path is hard to see, and Thor trips over a hidden root, stumbling forward.")
        print("They press on, but the uncertainty lingers...")
        chapter_4("light", None)
def lit_path(status):
    time.sleep(2)
    print("The sun shines down on the open path, making travel easier.")
    print("The path is peaceful, and Thor and Snow make progress.")
    chapter_4(path, weapon)
def chapter_4():
    print("We are almost there! Keep going.")