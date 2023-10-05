'''
We want to create an application for purchasing airplane tickets that receives the following information as inputs:

Age
Accompanied by mother
Accompanied by father
Passport
Mother's permission document
Father's permission document
Boarding conditions:
If the person is over 18 years old and has a passport
If the person is under 18 years old, has a passport, and is accompanied by both parents
If the person is under 18 years old, has a passport, is accompanied by at least one parent, and has written permission from the other parent
Write the code that implements the boarding conditions above and test it with all the variants that you think should be tested.
python

Generate test scenarios with expected results and then run the code to check if the expected results are equal to the actual results.
Examples:
Age 19, no passport => Cannot board
Age 17, has passport, both parents => Can board
'''
age = int(input("Please write the passenger age: "))
valid_passport = input("Is the passport valid? Yes/No ")
if age>=18 and valid_passport == "Yes":
    print("You can get onboard")
elif age<18 and valid_passport == "Yes":
    both_parents = input("Is the child accompanied by both parents? ")
    if both_parents == "Yes":
        print("You can get onboard")
    else:
        permission = input("Permission from missing parent: ")
        if permission == "Yes":
            print("You can get onboard")
        else:
            print("You can NOT get onboard")
else:
    print("You can NOT get onboard")

"""
Test scenarios:
Adult over 18 with a valid passport => Can board
Adult over 18 with an invalid passport => Cannot board
Child with a valid passport and both parents => Can board
Child with a valid passport and one parent - missing parent permission => Can board
Child with a valid passport and one parent - missing parent permission => Cannot board
Child without a valid passport => Cannot board
"""

# 2. Game of chance
# Search online and find out how to generate a random number
# Imagine that you are rolling a dice and save this number in a variable called "dice_roll". The saved number will be generated randomly using the method found online
# Enter a number from the keyboard to represent the user's chosen number
# Check and display if the user has guessed the number
# There will be 3 options that need to be handled:
# You lost. You chose a smaller number. You chose x but it was y.
# You lost. You chose a larger number. You chose x but it was y.
# You won. Congratulations! You chose x and the dice was y.

import random
dice_roll = random.randint(0, 6)
guess = int(input('Ghiceste zarul'))
if guess < dice_roll:
    print(f'You lost. You chose a smaller number. You chose {guess} but it was {dice_roll}')
elif guess > dice_roll:
    print(f'You lost. You chose a larger number. You chose {guess} but it was {dice_roll}.')
else:
    print(f'You won. Congratulations! You chose {guess} and the dice was {dice_roll}.')