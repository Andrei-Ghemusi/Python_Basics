
print('\n-------Ex_1---------')
#1. Function that calculates and returns the sum of 2 numbers
# cazul in care putem introduce numerele de la tastatura, e mai dinamic
x = int(input('Write the first number: '))
y = int(input('Write the second number: '))

def suma_numere(x, y):
    suma = x + y
    return (f'The sum of these two numbers is: {suma}')


print(suma_numere(x, y))


# with arguments when we call the function
def suma_numere(a, b):
    suma = a + b
    return (f'The sum of these two numbers is: {suma}')


print(suma_numere(8, 10))
print(suma_numere(78, 10))


print('\n-------Ex_2---------')
'''2. Function that returns TRUE if a number is even, FALSE for odd.'''
def par_impar(numar):  # we define the function and add the param "numar"
    if numar % 2 == 0:  # we verify if it is even
        return True
    else:
        return False


print(par_impar(84))
print(par_impar(75))


print('\n-------Ex_3---------')
'''3. Function that returns the total number of characters in your full name. (last name, first name, middle name) 
'''
def total_characters(nume, prenume1, prenume2):
    return len(nume + prenume1 + prenume2)

print(total_characters('Popescu', 'George', 'Dan'))


print('\n-------Ex_4---------')
'''4. Function that returns rectangle area'''
def area_rectangle(length, width):
    area = length * width
    return area

print(area_rectangle(8, 5))
print(area_rectangle(10, 45))


print('\n-------Ex_5---------')
'''5. Function that returns circle area'''
def area_circle(raza):
    area = raza * raza * 3.14
    return area

print(area_circle(6))
print(area_circle(10))


print('\n-------Ex_6---------')
'''6. Function that returns True if a character x is found in a given string. False if not.'''
def search_character(string, x):
    if x in string:
        return True
    else:
        return False

print(search_character('abc', 'a'))
print(search_character('abc', 'd'))


print('\n-------Ex_7---------')
'''7. Function without return, receives a string and prints on the screen: 
The number of lower case characters is x, 
The number of upper case characters is y. '''

def lower_upper(string):
    char_upper = 0
    char_lower = 0
    for char in string:
        if char.isupper():
            char_upper = char_upper + 1
        elif char.islower():
            char_lower = char_lower + 1
    print(f'The number of upper case characters is: {char_upper}')
    print(f'The number of lower case characters is: {char_lower}')

lower_upper('abc1ABCD!')


print('\n-------Ex_8---------')
'''8. Function that receives a LIST of numbers and returns a LIST with only the positive numbers.'''
lista_numere = [1, -4, 78, -5, 0, 85, 4, -10, -2]

def numbers_pozitive(numere):
    lista_numere_pozitive = []
    for number in numere:
        if number > 0:
            lista_numere_pozitive.append(number)
    return lista_numere_pozitive

print(numbers_pozitive(lista_numere))


print('\n-------Ex_9---------')
'''9. Function that doesn't return anything. Receives 2 numbers and PRINTS: 
First number x is greater than the second number y, 
Second number y is greater than the first number x, 
The numbers are equal.'''


def two_numbers(x, y):
    if x == y:
        print(f'The numbers are equal.')
    elif x > y:
        print(f'First number {x} is greater than the second number {y}')
    else:
        print(f'Second number {y} is greater than the first number {x}')


two_numbers(89, -5)
two_numbers(7, 46)


print('\n-------Ex_10---------')
'''10. Function that receives a number and a set of numbers. 
Prints 'added the new number to the set' + returns True 
or Prints 'did not add the number to the set. It already exists' + returns False.'''
set_numbers_input = {2, 5, 8, 78, -8, 45}

def add_numbers(set_numbers, new_number):
    if new_number in set_numbers:
        print(f'did not add the {new_number} in set, it already exists.')
        return False
    else:
        set_numbers.add(new_number)
        print(f'added {new_number} in set')
        return True

print(add_numbers(set_numbers_input, 78))
print(add_numbers(set_numbers_input, 75))


print('\n-------Ex_11---------')
'''11. Function that receives a month of the year and returns how many days that month has.'''
def calendar(month):
    all_months = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }
    if month in all_months:
        return all_months.get(month)

print(calendar('June'))
print(calendar('January'))
print(calendar('February'))


print('\n-------Ex_12---------')
'''
12. Calculator function that returns 4 values: Sum, difference, multiplication, and division of 2 numbers.
'''
def calculator(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d

a, b, c, d = calculator(3, 2)

print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)


print('\n-------Ex_13---------')
'''13. Function that receives 3 numbers and returns the maximum value among them.'''
def maxim(x, y, z):
    if x == y == z:
        return ('numbers are equal')
    elif x >= y and x >= z:
        return (f'{x} is the highest number')
    elif y >= x and y >= z:
        return (f'{y} is the highest number')
    else:
        return (f'{z} is the highest number')

print(maxim(20, 20, 2))
print(maxim(5, 100, 100))
print(maxim(7, 7, 7))
print(maxim(17, 2, 17))


print('\n-------Ex_14---------')
'''
14. Function that receives a list of digits (i.e., only 0-9) 
Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5] 
Returns a DICT that tells us how many times each digit appears.
'''
lista1 = [1, 1, 2, 7, 7, 7]

def count(lista):
    cnt = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    for i in cnt.keys():
        for j in lista:
            if i == j:
                cnt[i] = cnt[i] + 1
    return cnt

print(count(lista1))


print('\n-------Ex_15---------')
'''15. Function that receives 3 numbers and returns the maximum value among them. '''
def maxim(a, b, c):
    if a == b and b == c:
        max = a
    elif a >= b and a >= c:
        max = a
    elif b >= a and b >= c:
        max = b
    else:
        max = c
    return max

print(maxim(5, 7, 2))  # returns 7
print(maxim(7, 6, 2))  # returns 7
print(maxim(5, 6, 7))  # returns 7
print(maxim(4, 4, 4))  # returns 4
print(maxim(4, 3, 3))  # returns 4
print(maxim(3, 4, 3))  # returns 4
print(maxim(3, 3, 4))  # returns 4


print('\n-------Ex_16---------')
'''
16. Function that receives a number and returns the sum of all numbers from 0 to that number.
'''
def suma_num(a):
    suma = 0
    for i in range(0, a + 1):
        suma = suma + i
    return suma

print(suma_num(3))  # returns 6


print('\n-------Ex_17---------')
'''17. Function that receives 2 lists of numbers (numbers can be duplicated) and returns the common numbers.
Example:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Answer: {2, 3}
'''

list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]

def common_nr(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    return set1.intersection(set2)

print(common_nr(list1, list2))


print('\n-------Ex_18---------')
'''
18. Function that applies a discount price. 
If the product costs 100 lei and we apply a 10% discount, the price will be 90. 
Handle cases where the discount is invalid. For example, a 110% discount is invalid.
'''

def price_discount(price, sale):
    if sale > 100 or sale < 0:
        return 'reducere invalida'
    new_price = price - (sale / 100) * price
    return new_price

print(price_discount(100, 10))  # 90
print(price_discount(100, -1))  # no
print(price_discount(100, 101))  # no


print('\n-------Ex_19---------')
'''
19. Function that prints current date and time from Romania
'''
from datetime import datetime

def data_ora():
    date_time = datetime.now()
    dt_string = date_time.strftime("%d/%m/%Y %H:%M:%S")
    print("Date and Time: ", dt_string)

data_ora()


print('\n-------Ex_20---------')
'''20. Function that returns how many days are left until christmas:'''
from datetime import date

def until_xmas(year):
    christmas_day = date(year=year, month=12, day=25)
    days_til_christmas = (christmas_day - date.today()).days
    return days_til_christmas

print(until_xmas(2022))