"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martina Drobná
email: fiamar@seznam.cz
"""

import random

separator = 60 * "-"

print(" ")
print(f"Hi there!\n{separator}")
print(f"I've generated a random 4 digit number for you.")
print(f"Let's play a bulls and cows game.\n{separator}")


while True:
    """
    This program has generated 4 random digit number. The number 
    can't start with 0, can't contain the same number and must 
    contain only digit number.
    """
    numbers = random.randrange(1000, 9999)
    number = set(str(numbers))

    if len((number)) == len(str(numbers)):
        random_numbers = str(numbers)
        break   

count_guess = 0
"""
Counts how many attempts the user needed to
guess the number.
"""

while True:
    """
    The user has entered 4 random digit number. 
    The program notifies that:
    - the user has entered shorter or longer number, 
    - number can't start with 0, 
    - number can't contain the same number and 
    - must contain only digit number.
    """
    guess = input("Enter a number!\n")
    guess2 = set(guess)
    count_guess += 1
    if not len(guess) == 4:
        print("It doesn't contain 4 digit number.") 
        print(separator)       
    elif not guess.isdigit():
        print("It isn't number.")
        print(separator)    
    elif guess[0] == "0" and len(guess) == 4:
        print("Number can't start with 0.")
        print(separator)            
    elif len(guess2) != len(guess):
        print("It can't contain the same digit.")
        print(separator)    
    else:
        count_bulls = 0
        """
        It prints the count of numbers if the user guesses 
        both the number and its location correctly.
        """
        count_cow = 0
        """
        Prints the number of numbers if the user guesses 
        only the number but not its position
        """
         
        for position_number in range(len(guess)):
            if random_numbers[position_number] == guess[position_number]:
                count_bulls += 1

        for same_number in guess:
            if same_number in random_numbers:
                count_cow += 1
                count_cows = count_cow - count_bulls

        """
        It takes into account singular and plural in the output.
        (1 bull, 1 cow, but 2 bulls, 2 cows)
        """
        if count_bulls == 1 and count_cows == 1:
            print(f"{count_bulls} bull, {count_cows} cow")
            print(separator)
        elif count_bulls == 1 and count_cows != 1:
            print(f"{count_bulls} bull, {count_cows} cows")
            print(separator)
        elif count_bulls != 1 and count_cows == 1:
            print(f"{count_bulls} bulls, {count_cows} cow")
            print(separator)
        else:
            print(f"{count_bulls} bulls, {count_cows} cows")
            print(separator)
    

        if count_bulls == 4:                
            break
 
print(f"Correct, youv've guessed the right number in {count_guess} guesses.")
print(separator)
print("That's amazing!")
print(" ")
exit()

            

