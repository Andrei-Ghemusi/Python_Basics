# 1. Write a while loop that adds all the numbers up to 100 (inclusive).
numbers = 0
counter=0
total=0


while counter <= 100:
    total= total+counter
    counter= counter+1

print(total)

# 2. Using while loop, if statement and str() function; iterate through the list and if there is a 100,
# print it with its index number. i.e.: "There is a 100 at index no: 5"

i = 0
lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]

while i <len(lst):
    if lst[i] == 100:
        print("There is a 100 at index no: 5")
    i +=1


# 3. Using while loop and an if statement write a function named name_adder which appends all the elements in a list
# to a new list unless the element is an empty string: "".
lst1=["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]

def name_adder(list):
    i =0
    new_list =[]
    while i < len(list):
        if list[i] != "":
            new_list.append(list[i])
        i +=1
    return new_list

print(name_adder(lst1))


# 4. This time inside a function named name_adder, write a while loop that stops appending items to the new list as
# soon as it encounters an empty string: "". And prints "There is an empty string and returns the new list."

lst2=["Sam", "", "Ben", "Olivia", "Alicia"]

def name_adder(list):
    i = 0
    new_list=[]
    while i <len(list):
        if list[i] != "":
            new_list.append(list[i])
        else:
            break
        i += 1
    return new_list

print(name_adder(lst2))











