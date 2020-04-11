# -*- V1 (=1 after changfe in POSITION) -*-
"""
Created on Sat Apr 11 19:19:51 2020 for SPYNAV

@author: Viraj Shah!
"""
#-------------------------------------------------------------
import time

text = "Enter 'r' for going to the right. Enter 'l' for going to the left. Type 'u' for moving up. And type 'd' for moving down. Type in 'q' to quit the program."
user_in_get = input("a to continue. q to exit......")
user_pos_ver = 0
user_pos_hor = 0
user_in = ""

while user_in_get=="a":
    
    user_in = input(text)
    if user_in=="r":
        
        print("")
        user_pos_hor = user_pos_hor + 1
        print("Your current position = " + str(user_pos_ver) + ", " + str(user_pos_hor))
        time.sleep(2)
        
    elif user_in=="l":
        
        print("")
        user_pos_hor = user_pos_hor - 1
        print("Your current position = " + str(user_pos_ver) + ", " + str(user_pos_hor))
        time.sleep(2)
        
    elif user_in=="u":
        
        print("")
        user_pos_ver = user_pos_ver + 1
        print("Your current position = " + str(user_pos_ver) + ", " + str(user_pos_hor))
        time.sleep(2)
        
    elif user_in=="d":
        
        print("")
        user_pos_ver = user_pos_ver - 1
        print("Your current position = " + str(user_pos_ver) + ", " + str(user_pos_hor))
        time.sleep(2)
    

    
    elif user_in_get or user_in=="q":
        break
    