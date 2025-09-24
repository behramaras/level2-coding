# Import random module for generating random numbers
import random as rd

def createNumberList(N):
    numberList = []                 # Create an empty list

    for i in range(N):              # Loop N times
        number = rd.randint(1,100)  # Generate a random number between 1 and 100
        numberList.append(number)   # Append the number to the list

    return numberList               # Return the created list
    

def sortingList(arr):
    if len(arr) <= 1:                # If the list has 0 or 1 element, it's already sorted
        return arr

    reference = arr[-1]              # Choose the last element as reference
    left = [i for i in arr[:-1] if i <= reference]      # Elements <= reference go to the left
    right = [i for i in arr[:-1] if i > reference]      # Elements > reference go to the right

    return sortingList(left) + [reference] + sortingList(right)  # Recursively sort left and right, then combine

# Welcome message
print("*" * 57,"\n\tWelcome to The Sorting Numbers Machine!!!",
      "\n\t     Enter 'q' to exit!!!\n", "*" * 57, sep="")

# Ask the user for the number of elements
while True:
    N = input("\nEnter the amount of the numbers: ")

    if N.lower() == "q":        # If user enters 'q', exit the program
        print("Bye!!!")
        break
    if not N.isdigit():         # If input is not a number, ask again
        print("Please enter a number!!!")
        continue
    else:
        N = int(N)              # Convert input to integer
        if N == 0:              # If 0 is entered, show a message
            print("There is no number!!!")
        else:    
            arr = createNumberList(N)       # Generate a random number list
            sorted_arr = sortingList(arr)   # Sort the list
            print(f"Your original numbers: {', '.join(map(str, arr))}")
            print(f"Your sorted numbers: {', '.join(map(str, sorted_arr))}")
