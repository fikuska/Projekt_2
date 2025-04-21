import random

separator = 60 * "-"


numbers = list(range(0, 10))
random.shuffle(numbers)
if numbers[0] == 0:
    # The number can't start with 0
    # Change numbers[0] which beginn "0" behind numbers[4] 
    numbers[0] = numbers[4]
four_digit = (f"{numbers[0]}{numbers[1]}{numbers[2]}{numbers[3]}")
print(four_digit)
count_guess = 0

while True:
    count_guess += 1
    guess = str(input("Enter a number!\n"))
    guess2 = set(guess)

    def guess_number(user_number):
        if not len(user_number) == 4:
            return f"It doesn't contain 4 digit number."    
        elif not user_number.isdigit():
            return f"It isn't number."  
        elif user_number[0] == "0" and len(user_number) == 4:
            return f"Number can't start with 0."         
        elif len(guess2) != len(user_number):
            return f"It can't contain the same digit."  
    mistake = (guess_number(guess))


    def position(bull, cow):
        for position_number in range(len(guess)):
            if four_digit[position_number] == guess[position_number]:
                bull += 1
            if guess[position_number] in four_digit and four_digit[position_number] != guess[position_number]:
                cow += 1    
        def sing_plur():
            if bull == 1:
                return "bull"
            else:
                return "bulls"
        def plur_sing():
            if cow == 1:
                return "cow"    
            else:
                return "cows"
        return f"{bull} {sing_plur()}, {cow - bull} {plur_sing()}"
    count = position(0, 0)
    

  


    if count == "4 bulls, 0 cows":
        break

print(f"Correct, youv've guessed the right number in {count_guess} guesses.")
print(separator)
print("That's amazing!")
print(" ")
