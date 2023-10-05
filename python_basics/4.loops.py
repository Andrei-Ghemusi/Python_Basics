print('\n-------Ex_1---------')
#1 Having the list:
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Use a for loop to iterate through the entire list and print:
# ● 'My favorite car is x'.
# ● Do the same with a for each loop.
# ● Do the same with a while loop.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# using for
for i in range(len(masini)):
    print(f'FOR: My favourite car is: {masini[i]}')

# usin for each
for masina in masini:
    print(f'FOR EAACH: My favourite car is: {masina}')

# using while
i = 0
while i < len(masini):
    print(f'WHIE: My favourite car is: {masini[i]}')
    i = i + 1


print('\n-------Ex_12---------')
#2 The same list:
# Use a for else loop
# In the for loop:
# Modify the elements in the list so that they are written in uppercase, except for the first and last elements.
# In the else block:
# Print the list.
for masina in range(1, len(masini)-1): # moving from second postion to second to last
    masini[masina] = masini[masina].upper()

print(masini)


print('\n-------Ex_3---------')
#3 The same list:
# A buyer comes who wants to buy a Mercedes.
# Iterate through it using your preferred method.
# If the car is a Mercedes:
# Print 'I found the car you are looking for'
# Exit the loop using a keyword that does this
# Otherwise:
# Print 'I found car X. Still searching'
#
# (Note: I assume the task is to find the Mercedes in the list and exit the loop once it's found)
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print(f'I found the car you are looking for {masina}')
        break
    else:
        print(f'I found car {masina}. Still searching')


print('\n-------Ex_4---------')
#4 Same list;
# A wealthy but indecisive buyer is coming. We will present him with all the cars except Trabant and Lăstun.
# If the car is Trabant or Lăstun:
# Use a keyword that skips what follows (no need for else).
# Print "You might like car x."
for masina in masini:
    if masina == "Trabant" or masina == 'Lastun':
        continue
    print(f'You might like car {masina}.')


print('\n-------Ex_5---------')
#5 Update the car fleet:
# ● Create an empty list, masini_vechi.
# ● Iterate through mașini.
# ● When you find Lăstun or Trabant:
# Save these cars in masini_vechi.
# Overwrite them with 'Tesla' (in the original list of cars).
# ● Print Old models: x.
# ● New models: x.
masini_vechi = []

for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        masini_vechi.append(masina)
        index = masini.index(masina)
        masini[index] = 'Tesla'
print('Old models:', masini_vechi)
print('New models:', masini)


print('\n-------Ex_6---------')
#6 Given dict:
# car_prices = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# A client comes with a budget of 15000 euros.
# Present only the cars that fit within this budget.
# Iterate through dict.items() and access the car and price.
# Print "For a budget of under 15000 euros you can choose x car" for each car within the budget.
# Iterate through the list.
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget = 15000
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'For a budget of under {buget} euros you can choose {masina}.')


print('\n-------Ex_7---------')
#7 Having the list:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterate through the list.
# ● Print how many times 3 appears in the list (you are not allowed to use count).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

x = 0
for numar in numere:
    if numar == 3:
        x = x + 1
print(f'Number 3 occurs {x} times in list numere.')


print('\n-------Ex_8---------')
# #8 The same list:
# ● Iterate through it
# ● Calculate and print the sum of the numbers (you're not allowed to use sum).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma = suma + numar
print(f'Sum of all of the numbers in the list is: {suma}')


print('\n-------Ex_9---------')
#9 Same list:
# ● Iterate through it.
# ● Display the largest number (you are not allowed to use max).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#numere = [-3, -2, -1] # test, max can't be 0, it has to be an element from the list
max = numere[0]
for numar in numere:
    if numar > max:
        max = numar
print(f'Highest number in the list is: {max}')


print('\n-------Ex_10---------')
#10 The same list:
# ● Iterate through it.
# ● If the number is positive, replace it with its negative value.
# Ex: if it's 3, make it -3
# ● Display the new list.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lista_neg = []
for numar in numere:
    if numar > 0:
        numar = numar - numar*2
        #numar = -(abs(numar)) # another solution
    lista_neg.append(numar)
print(f'The list became: {lista_neg}')


print('\n-------Ex_11---------')
#11 alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterate through list alte_numere
# Populate the other lists correctly
# Print the 4 lists at the end
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'Lista cu numere pare este: {numere_pare}')
print(f'Lista cu numere impare este: {numere_impare}')
print(f'Lista cu numere pozitive este: {numere_pozitive}')
print(f'Lista cu numere negative este: {numere_negative}')


print('\n-------Ex_12---------')
#12 Bubble sort
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
    for j in range(i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
print(alte_numere)


print('\n-------Ex_13---------')
#13 Number guessing game:
# secret_number = Generate a random number between 1 and 30
# guessed_number = None
# Using a while loop
# User chooses a number
#
# The program tells them:
# ● Secret number is greater
# ● Secret number is smaller
# ● Congratulations! You guessed it!
import random

secret_number = random.randint(1, 30)
guessed_number = None
while guessed_number is None:
    nr = int(input('Write a number: '))
    if nr > secret_number:
        print('Secret number is smaller')
    elif nr < secret_number:
        print('Secret number is higher')
    else:
        print('Congrats, you got it!')
        break


print('\n-------Ex_14---------')
#14 Input a number
# Write a program that will generate in console a pyramid like this:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
num = int(input("Give a nr: "))
i = 1
for i in range(1, num+1):
    for j in range(i):
        print(i, end="")
    print()


print('\n-------Ex_15---------')
#15 Iterate through the list using nested loops
# Print 'The current digit is:"
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'The current digit is: {tastatura_telefon[i][j]}')

# using for each
for row in tastatura_telefon:
    for column in row:
        print(f'FOR EACH: The current digit is: {column}')








