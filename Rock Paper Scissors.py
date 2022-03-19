import random

user_wins = 0
bot_wins = 0

options = ["rock", "paper", "scissors", "r", "p", "s"]

while True:
    user_input = input("Type Rock/Paper/Scissors or R/P/S or Q to quit:  ").lower()
    if user_input == "q":
        break
    
    if bot_wins == 10 or user_input == 10:
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    bot_pick = options[random_number]
    print("Bot picked ", bot_pick)

    if user_input == "rock" or user_input == "r" and bot_pick == "scissors" or bot_pick == "s":
        print("You scored!!")
        print("")
        user_wins += 1
        continue

    elif user_input == "paper" or user_input == "p" and bot_pick == "rock" or bot_pick == "r":
        print("You scored!!")
        print("")
        user_wins += 1
        continue

    elif user_input == "scissors" or user_input == "s" and bot_pick == "paper" or bot_pick == "p":
        print("You scored!!")
        print("")
        user_wins += 1
        continue

    elif user_input == "rock" or user_input == "r" and bot_pick == "rock" or bot_pick == "r":
        print("No one Scored")
        print("")
        continue

    elif user_input == "paper" or user_input == "p" and bot_pick == "paper" or bot_pick == "p":
        print("No one Scored")
        print("")
        continue

    elif user_input == "scissors" or user_input == "s" and bot_pick == "scissors" or bot_pick == "s":
        print("No one Scored")
        print("")
        continue

    else:
        print("Bot scored!")
        print("")
        bot_wins += 1
        continue

print("You scored ", user_wins, " points")   
print("Bot scored ", bot_wins, " points")  

print("Goodbye!..")