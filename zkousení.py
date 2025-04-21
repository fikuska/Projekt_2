import random

separator = 60 * "-"

def main():
    print(" ")
    print(f"Hi there!\n{separator}")
    print(f"I've generated a random 4 digit number for you.")
    print(f"Let's play a bulls and cows game.\n{separator}")

    # Generating four-digit number
    numbers = list(range(0, 10))
    random.shuffle(numbers)
    if numbers[0] == 0:
        # The number can't start with 0
        # Replace numbers[0] that starts with "0" with 
        # numbers[1] and vice versa
        numbers[0], numbers[1] = numbers[1], numbers[0]
    four_digit = (f"{numbers[0]}{numbers[1]}{numbers[2]}{numbers[3]}")

    count_guess = 0

    while True:
        count_guess += 1
        guess = str(input("Enter a number!\n"))

        def guess_number(user_number: str) -> str:
            """Checked that:
                - the user has entered shorter or longer number,
                - number can´t start with 0,
                - number can´t contain the same number ane
                - must contain only digit number.
            """
            if not len(user_number) == 4:
                return f"It doesn't contain 4 digit number."    
            elif not user_number.isdigit():
                return f"It isn't number."  
            elif user_number[0] == "0" and len(user_number) == 4:
                return f"Number can't start with 0."         
            elif len(set(user_number)) != len(user_number):
                return f"It can't contain the same digit."     
        mistake = (guess_number(guess))

        if mistake:
            print(mistake)
            print(separator)
        else:
            def position(bull: int, cow: int) -> str:
                """
                Bull prints the count of numbers if the user guessed
                both the number and its location correctly.
                Cow prints the number of numbers if the user guessed
                only the number but not its position.
                """
                for position_number in range(len(guess)):
                    if four_digit[position_number] == guess[position_number]:
                        bull += 1
                    if (
                        guess[position_number] in four_digit and 
                        four_digit[position_number] != guess[position_number]
                    ):
                        cow += 1    
                def sing_plur() -> str:
                    """
                    It takes into account singular and plural in the output.
                    (1 bull but 3 bulls)
                    """
                    if bull == 1:
                        return "bull"
                    else:
                        return "bulls"
                def plur_sing() -> str:
                    """
                    It takes into account singular and plural in the output.
                    (1 cow but 3 cows)
                    """
                    if cow == 1:
                        return "cow"    
                    else:
                        return "cows"
                return f"{bull} {sing_plur()}, {cow} {plur_sing()}"
            count = position(0, 0)
            print(count)
            print(separator)

            if count == "4 bulls, 0 cows":
                break

    print(f"Correct, you've guessed the right number in {count_guess} guesses.")
    print(separator)
    print("That's amazing!")
    print(" ")

if __name__ == "__main__":
    main()


