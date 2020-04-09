"""MADE BY: VIRAJ SHAH"""
"""robomitra@gmail.com"""




import random
import time

ladders = {
    
    9,
    56,
    86,
    30,
    6,
    13,
    39,
    50,
    45
    
    }
snakes = {
    
    
    99,
    65,
    77,
    19,
    16,
    26,
    56,
    89,
    33
    
    }

end= 100
get = ""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

p1_init_pos = 0
p2_init_pos = 0

p1_final_pos = 0
p2_final_pos = 0

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

print("THIS IS A SNAKE GAME")
print("Made by Viraj Shah")
print("")
print("First you have to enter your names")
time.sleep(1.3)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

p1 = input("Enter the name of the first player:  ")
time.sleep(1.3)
p2 = input("Enter the name of the second player:  ")
time.sleep(1.3)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print("")
print("Now, press enter to roll the dice.")
print("")

while 1==1:
    pal1 = input(p1 + ", Press enter to roll the dice:  ")
    print("")
    
    p1_dice = random.randint(1, 6)
    print("You rolled, " + str(p1_dice))
    p1_final_pos = p1_init_pos + p1_dice
    
    print(p1 + " moved from " + str(p1_init_pos) + " to " + str(p1_final_pos))
    p1_init_pos = p1_final_pos
    p1_final_pos = 0
    print("")
    
    if p1_init_pos in snakes:
        print("Snake bite ~~~~~~~~~~")
        deduct = random.randint(1, 15)
        p1_final_pos = p1_init_pos - deduct
        print("")
        
        print(p1 + " went down from " + str(p1_init_pos) + " to " + str(p1_final_pos))
        p1_init_pos = p1_final_pos
        p1_final_pos = 0
        
    elif p1_init_pos >= end:
        get = "a"
        break
    
    elif p1_init_pos in ladders:
        print("Wow" or "You got a ladder" or "Congo, a ladder")
        add = random.randint(1, 15)
        p1_final_pos = p1_init_pos + add
        print("")
        
        print(p1 + " went up from " + str(p1_init_pos) + " to " + str(p1_final_pos))
        
        p1_init_pos = p1_final_pos
        p1_final_pos = 0
        
    time.sleep(0.5)
    
    """"""""""""""""""""""""""""""""""""""""""
    
    pal2 = input(p2 + ", Press enter to roll the dice:  ")
    print("")
    
    p2_dice = random.randint(1, 6)
    print("You rolled, " + str(p2_dice))
    print("")
    p2_final_pos = p2_init_pos + p2_dice
    
    print(p2 + " moved from " + str(p2_init_pos) + " to " + str(p2_final_pos))
    print("")
    
    p2_init_pos = p2_final_pos
    p2_final_pos = 0
    
    if p2_init_pos in snakes:
        print("Snake bite ~~~~~~~~~~")
        print("")
        deduct = random.randint(1, 15)
        p2_final_pos = p2_init_pos - deduct
        print("")
       
        print(p2 + " went down from " + str(p2_init_pos) + " to " + str(p2_final_pos))
        p2_init_pos = p2_final_pos
        p2_final_pos = 0
        
    elif p1_init_pos >= end:
        get = "b"
        break
    
    elif p1_init_pos in ladders:
        print("Wow" or "You got a ladder" or "Congo, a ladder")
        print("")
        add = random.randint(1, 15)
        p1_final_pos = p1_init_pos + add
        print("")
        print(p2 + " went up from " + str(p2_init_pos) + " to " + str(p2_final_pos))
        
        p1_init_pos = p1_final_pos
        p1_final_pos = 0
        
    time.sleep(0.5)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print("Game over")
print("")
if get=="a":
    print(p1 + " wins! Congratulations!")
else:
    print(p2 + " wins! Congo!")



