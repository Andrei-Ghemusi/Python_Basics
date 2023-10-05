
'''
1. Class Circle
Attributes: radius, color
Constructor for both attributes
Methods:
● describe_circle() - will PRINT the color and radius
● area() - will RETURN the area
● diameter()
● circumference()
'''
class Circle:

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
        self.PI = 3.14

    def describe_circle(self):
        print(f'The radius is: {self.raza}')
        print(f'The color of the circle is: {self.culoare}')

    def area(self):
        self.area = self.PI * self.raza ** 2
        return self.area

    def diameter(self):
        self.diam = self.raza * 2
        return self.diam

    def circumference(self):
        return self.diam * self.PI


'''
2. Class Rectangle
Attributes: length, width, color
Constructor for all attributes
Methods:
● describe()
● area()
● perimeter()
● change_color(new_color) - this method does not return anything. 
It takes a new color as a parameter and will overwrite the attribute self.color. 
You can check the color change by calling the describe() method.
'''
class Rectangle():

    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def describe(self):
        print(f'Lungimea este {self.length}!')
        print(f'Latimea este {self.width}!')
        print(f'Culoarea este {self.color}!')

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def change_color(self, new_color):
        self.color = new_color


'''
3. Class Employee
Attributes: name, surname, salary
Constructor for all attributes
Methods:
● describe()
● full_name()
● monthly_salary()
● annual_salary()
● increase_salary(percent)
'''
class Employee():

    def __init__(self, last_name, first_name, salary):
        self.last_name = last_name
        self.first_name = first_name
        self.salary = salary

    def describe(self):
        print(f"Employee's name is {self.last_name}")
        print(f"Employee's first name is {self.first_name}")
        print(f"Employee's salary is {self.salary}")

    def full_name(self):
        return self.last_name + ' ' + self.first_name

    def monthly_salary(self):
        return self.salary

    def annual_salary(self):
        return 12 * self.salary

    def increase_salary(self, percent):
        self.salary = self.salary + (percent / 100 * self.salary)


'''
Class Account
Attributes: iban, account_holder, balance
Constructor for all attributes
Methods:
● display_balance() - The account holder x has a balance of n lei in the account y
● withdraw(amount)
● deposit(amount)
'''
class Account:

    def __init__(self, iban, account_holder, balance):
        self.iban = iban
        self.account_holder = account_holder
        self.balance = balance

    def describe(self):
        print(f'Your IBAN is: {self.iban}')
        print(f'The account holder is: {self.account_holder}')
        print(f'Balance: {self.balance}')

    def display_balance(self):
        print(f'The account holder {self.account_holder} has a balance of {self.balance} lei, in the account {self.iban} !')

    def withdraw(self, sum):
        if sum >= self.balance:
            self.balance -= sum
        else:
            print('Fonduri insuficiente')

    def deposit(self, suma):
        self.balance += suma


'''
5. Class Invoice
Attributes: series (constant, no need for constructor, all invoices will have the same series), number, product_name, quantity, price_per_unit
Constructor: all attributes except series
Methods:
● change_quantity(quantity)
● change_price(price)
● change_product_name(name)
● generate_invoice() - will print the table if you can
'''
# pip install tabulate
from datetime import date
from tabulate import tabulate

class Invoice:
    series = 123456

    def __init__(self, number, product_name, quantity, price_per_unit):
        self.number = number
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def change_quantity(self, quantity):
        self.quantity = quantity

    def change_price(self, price):
        self.price_per_unit = price

    def change_product_name(self, name):
        self.product_name = name

    def calc_total(self):
        return self.price_per_unit * self.quantity

    def generate_invoice(self):
        print(tabulate([[self.product_name, self.quantity, self.price_per_unit, self.calc_total(), date.today()]],
                       headers=['Product', 'Quantity', 'Price per unit', 'Total', 'Date']))


'''
6. Class Car
Attributes: brand, model, maximum_speed, current_speed, color, available_colors (set), registered (bool)
Color = grey - all cars come out of the factory in grey color
Current_speed = 0 - all cars stay stationary when they come out of the factory
Available colors = choose 5-7 colors
Brand = choose - the factory produces a single brand but multiple models
Registered = False
Constructor: model, maximum_speed
Methods:
● describe() - all attributes will be printed, except available_colors
● register() - will change the registered attribute to True
● paint(color) - the car will be painted in the new color ONLY if the new color is in the available colors option, otherwise, display an error
● accelerate(speed) - the car will accelerate to a certain speed, if the speed is negative - error, if the speed is greater than maximum_speed - the car will accelerate to the maximum speed
● brake() - the car will stop and have a speed of 0.
'''
class Car:
    brand = 'Dacia'
    current_speed = 0
    color = 'grey'
    available_colors = ['red', 'green', 'white', 'blue', 'orange', 'black', 'yellow']
    registered = False

    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed

    def describe(self):
        print(f'The brand is: {self.brand}')
        print(f'The model is: {self.model}')
        print(f'Max speed is: {self.max_speed}')
        print(f'Current speed is: {self.current_speed}')
        print(f'The color is: {self.color}')
        print(f'The car is registered: {self.registered}')

    def register(self):
        self.registered = True
        return self.registered

    def paint(self, noua_culoare):
        if noua_culoare in self.available_colors:
            self.color = noua_culoare
            print(f'The new color of the car is: {self.color}')
        else:
            print('The color you chose is not available')

    def accelerate(self, viteza_dorita):
        if viteza_dorita < 0:
            print('ERROR!')
        elif viteza_dorita >= self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = viteza_dorita
        print(f'Current speed is: {self.current_speed}')

    def brake(self):
        self.current_speed = 0
        print(f'Current speed is: {self.current_speed}. We stopped.')


'''
7.Class TodoList
Attributes: todo (dictionary, where key is task name and value is task description)
Initially, the dictionary is empty, so no constructor is needed.

Methods:
● add_task(name, description) - adds a task to the dictionary
● complete_task(name) - removes a task from the dictionary
● show_todo_list() - prints only the keys (task names)
● show_additional_details(task_name) - depending on the task name, prints additional details.
○ If the task is not in the todo list, ask the user if they want to add it.
○ If they answer no - goodbye
○ If they answer yes - ask for task details and save the name and details to the dictionary
'''
class ToDoList:
    dict = {}

    def add_task(self, task_name, task_description):
        self.dict[task_name] = task_description
        print('I successfully added the task.')

    def complete_task(self, task_name):
        del self.dict[task_name]

    def show_todo_list(self):
        print(f'The tasks from TODO are: {self.dict.keys()}')

    def show_additional_details(self, task_name):
        if task_name in self.dict:
            print(f'The details for {task_name} are: {self.dict[task_name]}')
        else:
            print('I did not find the task')
            answer= input('Do you want to add the task in the list?')
            if answer.lower() == 'yes':
                task_description = input('Write a description for the new task: ')
                self.dict[task_name] = task_description
                print('I successfully added the task.')
            elif answer.lower() == 'no':
                print('Bye!')