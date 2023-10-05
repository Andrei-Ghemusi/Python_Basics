
# Ex:1 Explain how an if else works:
"""
if condition = True
    this block of code executes
else
    this block of code executes
"""

print('\nEx_2')
# Ex:2 - Verify and show if x is a natural number.
x = 3
if x >= 0 and type(x==int):
    print(f"{x} is a natural number")
else:
    print(f"{x} is not a natural number")


print('\nEx_3')
# Ex:3 - Verify and show if x is a positive, negative or neutral number.
x = 5
if x > 0:
    print('Number is positive')
elif x < 0:
    print('Number is negative')
else:
    print('Number is neutral')


print('\nEx_4')
# Ex:4 - Verify and show if x is inbetween -2 and 13 (including -2 and 13).
x = 3
if (x >= -2) and (x <= 13):
    print('This number is inbetween -2 si 13. ')
else:
    print('This number is not inbetween -2 si 13')


print('\nEx_5')
# Ex:5 - Verify and show if the difference between x and y is lower than 5.
x = 13
y = 8
if x - y < 5:
    print('The difference is lower than 5.')
else:
    print('The difference is not lower than 5.')


print('\nEx_6')
# Ex:6 - Verify if x is NOT inbetween 5 and 27 (including 5 and 27).
x = 4
if not (5 <= x <= 27):
    print('The number is not inbetween 5 and 27.')


print('\nEx_7')
# Ex:7 - Input two new integers y and x, then verify if they are equal, if not show which is higher.
x = int(input('Enter number for x: '))
y = int(input('Enter number for y: '))
if x == y:
    print(f"Numbers {x} and {y} are equal.")
elif x > y:
    print(f"{x} is higher than {y}.")
else:
    print(f"{y} is higher than {x}.")


print('\nEx_8')
# Ex:8 - Having integers x, y, z - all triangle sides,
                    # show if the triangle is isosceles (two sides are equal),
                    # equilateral (all sides are equal)
                    # no side is equal to another.
x = 4
y = 4
z = 4
if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
    print('Triangle is isosceles.')
elif x == y == z:
    print('Triangle is equilateral.')
else:
    print('Sides are not equal to one another.')


print('\nEx_9')
# Ex:9 - Input a letter then verify if it is a vowel or not.
letter = input('Write a letter: ')
letter = letter.lower()
if letter.isdigit():
    print('You did not input a letter, but you did input something?')
elif letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print('Letter is a vowel.')
else:
    print('Letter is not a vowel.')

print('\nEx_10')
# Ex:10 Transform the grades from the romanian grading system to the US grading system as follows:
# Over 9 => A
# Over 8 => B
# Over 7 => C
# Over 6 => D
# Over 4 => E
# 4 or under => F

nota = float(input("Write the received grade: "))
if 9 < nota <= 10:
    nota = "A"
    print(f"The received grade in the US grading system would be: {nota}")
elif nota >= 8:
    nota = "B"
    print(f"The received grade in the US grading system would be: {nota}")
elif nota >= 7:
    nota = "C"
    print(f"The received grade in the US grading system would be: {nota}")
elif nota >= 6:
    nota = "D"
    print(f"The received grade in the US grading system would be: {nota}")
elif nota > 4:
    nota = "E"
    print(f"The received grade in the US grading system would be: {nota}")
elif 4 >= nota >= 0:
    nota = "F"
    print(f"The received grade in the US grading system would be: {nota}")
else:
    print('You did not write a grade ranging from 1 to 10.')


print('\nEx_11')
# Ex:11 - Verify if x has a minimun of 4 digits.
x = int(input('Write a number to check if it has a minimum of 4 digits: '))
if x > 999:
    print(f'{x} does have 4 digits')
else:
    print(f'{x} does not have 4 digits')


print('\nEx_12')
# Ex:12 - Verify if x has exactly 6 letters.
x = 125645
if len(str(x)) == 6:
    print(f'{x} has exactly 6 letters')
else:
    print(f'{x} does not have 6 letters')


print('\nEx_13')
# Ex:13 - Verify if x is even or odd.
x = 44
if x % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")


print('\nEx_14')
# # Ex:14 Between integers x, y, z show which is the highest.
x = 4
y = 4
z = 2
if x >= y and x >= z:
    print(f'{x} is the highest')
elif y >= x and y >= z:
    print(f'{y} is the highest')
else:
    print(f'{z} is the highest')


print('\nEx_15')
# Ex:15 -  Having integers x, y, z - all triangle angles, verify and show if the triangle is valid (if the sum of all angles is 180 degrees)
x = 50
y = 18
z = 30
if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print('Triangle is valid.')
else:
    print('Triangle is not valid.')


print('\nEx_16')
# Ex:16
# Having the string: 'Coral is either the stupidest animal or the smartest rock' input a number x, then show the string without the last x characters.
string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Show how many characters you want to cut from the end: '))
print(string[0:-x])


print('\nEx_17')
# Ex:17
# Using the same string from ex_16, declare a new string made from the first 5 characters and the last 5.
string = 'Coral is either the stupidest animal or the smartest rock'
string1 = string[0:5]
string2 = string[-5:]
print(f'{string1}{string2}')


print('\nEx_18')
# Ex:18
'''
Using the same string from ex_16, declare in a variable and show the index of 'rock'.
            - using a variable and slicing, show the whole string until this word
            Expected output: 'Coral is either the stupidest animal or the smartest ' 
'''
string = 'Coral is either the stupidest animal or the smartest rock'
index_rock = string.index('rock')
print(string[:index_rock])


print('\nEx_19')
# Ex: 19
# Input a string then verify if the first and the last character are the same using an 'assert'

word = input('Choose a string to compare the first and the last character: ')
assert word[0].lower() == word[len(word)-1].lower(), 'First and last characters are different.'


print('\nEx_20')
# Ex: 20
# Having the STRING '0123456789' show only even digits and then show only odd the odd ones
word = '0123456789'
print(word[0::2])
print(word[1::2])












