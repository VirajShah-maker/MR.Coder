
import random

i = 0
user_score = 0
com_score = 0

print("WELCOME TO THE ROCK PAPER SCISSORS GAME")
    
print("You are playing against a computer. It is best of three.")
print(" ")
for i in range(3):
    ran = ["rock", "paper", "scissors"]
    com_guess = random.choice(ran)
    
    guess = input("ROCK or PAPER or SCISSORS?  ")
    
    print("You played, " + guess)
    print("The computer played " + com_guess)
    
    if com_guess==guess:
        print("IT IS A TIE!")
        i == i + 1
    else:
        if guess == "rock":
            if com_guess == "scissors":
                print("Congrats! YOU WON :)")
                i == i + 1
                user_score = user_score + 1
            elif com_guess == "paper":
                print("You lost :( ")
                com_score = com_score + 1
                i == i + 1
        elif guess == "paper":
            if com_guess == "rock":
                print("CONGRATS! You won :)")
                user_score = user_score + 1
                i == i + 1
            elif com_guess== "scissors":
                print("You lost :(")
                com_score = com_score + 1
                i == i + 1
        elif guess == "scissors":
            if com_guess == "paper":
                print("You won :)")
                user_score = user_score + 1
                i == i + 1
            elif com_guess== "rock":
                print("You lost :(")
                com_score = com_score + 1
                i == i + 1

print("")
print("Your score = " + str(user_score))
print("Computer score = " + str(com_score))
if com_score > user_score:
    print("Computer Wins :( ")
elif com_score==user_score:
    print("Its a TIE :)")
elif com_score < user_score:
    print("You WON!")