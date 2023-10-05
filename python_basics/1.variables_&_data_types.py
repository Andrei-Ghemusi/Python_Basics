#Ex_1 - Explain what a variable is.
"""
Variables are containers for storing data values.
"""

#Ex_2 - Write a variable for each of these: string, int, float, boolean.
country = "Romania" 		    #string variable
nr = 1 						#integer variable
number = 1.8 				#float variable
y = True					#boolean variable.

print('\nEx 3')
#Ex_3 - Using type function, check if the above variables have de expected data type.
print(type(country))
print(type(nr))
print(type(number))
print(type(y))

print('\nEx 4')
#Ex_4 - Round the float variable using the round() function and save this modification in the same variable (overwrite).
					# then verify again it's type of data
rounded_number = round(number)
print(rounded_number)
print(type(rounded_number))

print('\nEx 5')
#Ex_5 -  Using the print() function print in console 4 phrases using the 4 previously declared variables.
name = "Ioana"
years = 2.5
remaining_days = 30
hours = 4
print(f"{name} has been living in Spain for {y} years.")
print(f"{name} is older than her sister with {years} years. ")
print(f"There are {remaining_days} days left until {name} leaves. ")
print(f"{name} works {hours} hours a day.")

print('\nEx 6')
#Ex_6 - Input the name and surname of a person and save each of them in a different variable.
				# Show in console the next phrase:'My complet name has x characters'.
name_input = input('My name is: ')
surname_input = input('My surname is: ')
print(f'My complete name has {len(name_input) + len(surname_input)} caractere')

print('\nEx 7')
#Ex_7 - Input the length and width of a rectangle and save each of them in different variables.
				# Show in console the next phrase: 'Rectangle area is x square meters'.
lungimea = int(input('Rectangle length is: '))
latimea = int(input('Rectangle width is: '))
print(f'Rectangle area is {lungimea * latimea} square meters.')

print('\nEx 8')
#Ex_8 - Given the string: 'Coral is either the stupidest animal or the smartest rock' show how many times the word ' the ' appears.
prop ='Coral is either the stupidest animal or the smartest rock'
print(prop.count(' the '))

print('\nEx 9')
#EX_9 Using the string from Ex_8, replace 'the' with 'THE' (including 'the' from 'either').
prop ='Coral is either the stupidest animal or the smartest rock'
print(f'{prop.replace("the", "THE")}')

print('\nEx 10')
#Ex_10 Using the string from Ex_8, with an assert verify if this string contains ONLY numbers.
prop ='Coral is either the stupidest animal or the smartest rock'
try:
    assert prop.isdigit() == True
except:
    print('ERROR, phrase does not have only numbers')   # Here I used try/except because otherwise the code would crack/fail and stop all the other exercises
                                                        # I could have made the 'assert' be False, and no error would have been raised.


print('\nEx 11')
#Ex_11 Input an odd string and show the middle character.
					# It won't verify if the string is odd (assuming that we will introduce the correct number of characters),
text = str(input('Write an ODD string: '))
print(f'The middle character is: {text[(len(text)//2)]}')


#Ex_12 Using assert, verify if a string is a palindrome.
text = 'ana'
assert text == text[::-1], 'The string is not a palindrome'


print('\nEx 13')
#Ex_13 - Input a string (ex: 'alabala portocala') on which you shall do:
# save each word in a variable;
# print both variables to verify.
text = str(input('Write a string with two words: '))
x, y = text.split(' ')
print(f'First word is: {x}')
print(f'Second word is: {y}')

print('\nEx 14')
#Ex_14 - Input a string (ex: 'alabala portocala') on which you shall do:
# save first character in a variable;
# Uppercase this character everywhere, except the first and last character => alAbAlA portocAla.
text = str(input('Write a string with two words: '))
string_modificat = text[0]+text[1:len(text)-1].replace(x,x.upper())+text[len(text)-1]
print(string_modificat)

print('\nEx 15')
#Ex_15 - Input a user and a password. Print 'Password for the user x is ***** and it has y characters'.
user = str(input('User: '))
password = str(input('Password: '))
password_hidden = '*' * len(password)
print(f'Passord for user {user} is {password_hidden} and it has {len(password)} characters')