#Martha Moreno Gonzalez
#chapter 5:The Lake of Reflections

import time

def cahpter_5():
    print("Chapter 5: THe Lake of Refelctions") #working name. Not sold yet. 
    time.sleep(5)
    print("Thor and Snow just defeted the boss, out of breath the look onward.")
    print("Mesmerized by by their view there is a sense of peace in the air and something else...")
    print("There is hesitation in both Thor and Snow on what to do next.")

    print("What will you do?")
    print("1. Investigate the lake.")
    print("2. Pull Snow and jump into the water.")
   
    choice = input("Choose 1 or 2: ").strip()
    
    if choice == "1":
        investigate_lake()
    elif choice == "2":
        jump_in_water()
    else:
        print("Invalid choice. Try again.")
        chapter_5()
def investigate_lake():
    time.sleep(2)
    print("Thor and Snow lean over the water, gazing at their reflections.")
    print("The water does not change, only showing their true selves.")
    print("They exchange a small smile, understanding they have all they need.")
    print("*The screen fades to black.*")
    the_end()

def jump_in_water():
    time.sleep(2)
    print("Thor grabs Snow’s hand and they leap into the lake, water splashing everywhere.")
    print("Laughter fills the air as they splash and play, embracing the moment.")
    print("The future is uncertain, but for now, they are happy.")
    print("*The screen fades to black.*")
    the_end()

def the_end():
    time.sleep(2)
    print("In a world of uncertainty always make sure to embrace what you have now,")
    print("Nothing is ever guarantee, so keep working hard, keep adventuring.")
    time.sleep(5)
    print("THE END <3")