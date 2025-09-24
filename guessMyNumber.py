import random as rd

number = rd.randint(1,99)
attempt = 0
max_attempt = 10

print("*" * 47,"\n\tWelcome to The Number Guess Game!!!",
      "\n\t     You have 10 attempts!!!",
      "\n\t     Enter 'q' to exit!!!\n", "*" * 47, sep="")

while attempt < max_attempt:
    guess = input("Enter your guess: ")
    print(f"DEBUG: guess={repr(guess)}")
    if guess.lower() == "q":
        print("See you again!!!")
        break

    if not guess.isdigit():
        print("Please enter a valid number between 1 and 99!!!\n")
        continue
    
    guess = int(guess)

    if not (1 <= guess <= 99):
        print("Please enter a valid number between 1 and 99!!!\n")
        continue
    
    attempt += 1

    if guess == number:
        print(f"You are correct!!! The number is {number}!!!")
        break

    if attempt == max_attempt:
        print(f"\nAttempt: {attempt}.\nYou lost!!! The correct number was {number}.")

    elif guess < number:
        print(f"\nAttempt: {attempt}.\nToo low!!! Try again!!!\n")
    
    else:
        print(f"\nAttempt: {attempt}.\nToo high!!! Try again!!!\n")