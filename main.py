"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martina Drobná
email: fiamar@seznam.cz
"""

import random
separator = "-" * 60

def guess_number(user_number: str) -> str | None:
    """Validates user input:
    - number must have exactly 4 digits,
    - number can´t start with 0,
    - number can´t contain repeated digits,
    - must contain only digit characters.
    Return error message as string if invalid, otherwise None.
    """
    if not len(user_number) == 4:
        return f"It doesn't contain 4 digit number."    
    elif not user_number.isdigit():
        return f"It isn't number."  
    elif user_number[0] == "0":
        return f"Number can't start with 0."         
    elif len(set(user_number)) != len(user_number):
        return f"Number can't contain repeated digits."
    return None

def position(user_guess: str, random_digit: str) -> tuple[int, int]:
    """
    Returns a tuple (bulls, cows):
           -  bulls = correct digit and correct position.
           -  cows = correct digit, wrong position.
    """
    bull = 0
    cow = 0
    for position_number in range(len(user_guess)):
        if random_digit[position_number] == user_guess[position_number]:
            bull += 1
        elif (
            user_guess[position_number] in random_digit and
            random_digit[position_number] != user_guess[position_number]
            ):
            cow += 1 
    return bull, cow

def sing_plur(count_bulls: int) -> str:
    """
    Returns the correct singular /. plural form for 'bull'.
    (1 bull but 3 bulls)
    """
    if count_bulls == 1:
        return "bull"
    else:
        return "bulls"

def plur_sing(count_cows: int) -> str:
    """
    Returns the correct singular /. plural form for 'cow'.
    (1 cow but 3 cows)
    """
    if count_cows == 1:
        return "cow"    
    else:
        return "cows"

def game_bulls_cows() -> None:
    print(" ")
    print(f"Hi there!\n{separator}")
    print(f"I've generated a random 4 digit number for you.")
    print(f"Let's play a bulls and cows game.\n{separator}")

    # Generating random 4-digit number with no repeats and not starting with 0.
    numbers: list[int] = list(range(0, 10))
    random.shuffle(numbers)
    if numbers[0] == 0:
        numbers[0], numbers[1] = numbers[1], numbers[0]
    four_digit: str = f"{numbers[0]}{numbers[1]}{numbers[2]}{numbers[3]}"

    count_guess: int = 0

    while True:
        count_guess += 1
        guess = input("Enter a number!\n")

        mistake = guess_number(guess)
        if mistake:
            print(mistake)
            print(separator)
        else:
            count_bull, count_cow = position(guess, four_digit)
            bulls = sing_plur(count_bull)
            cows = plur_sing(count_cow)
            print(f"{count_bull} {bulls}, {count_cow} {cows}")
            print(separator)

            if count_bull == 4:
                break

    print(f"Correct, you've guessed the right number in {count_guess} guesses.")
    print(separator)
    print("That's amazing!")
    print(" ")

if __name__ == "__main__":
    game_bulls_cows()
            

