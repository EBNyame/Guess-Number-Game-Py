import random
print()
print("-------------------------------------------------------------------")
print("                       GUESS THE NUMBER GAME                       ")
print("-------------------------------------------------------------------")

user_number = -1
computer_number = random.randint(0, 100)
while user_number != computer_number:
    user_number = int(input("Enter a number from 0 to 100: "))
    if computer_number == user_number:
        print("Congratulation...you guessed correctly!!!")
    elif user_number < computer_number:
        print("WRONG...Guess higher!")
    elif user_number > computer_number:
        print("WRONG...Guess lower!")
