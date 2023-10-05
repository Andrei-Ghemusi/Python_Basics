"""

"""
print('\n-------Ex_1---------')
# Ex_1. Declare a list named "musical_notes" and add the notes "do re mi" etc. until "do"
# Print the list
# Reverse the order of the list using slicing and overwrite the original list
# Print the current version of the list (reversed)
# Apply a method to the list that you suspect does the same thing, i.e., reverse its order.
# Print the current version of the list. You should be back to the original version.
# Conclusion: Slicing is temporary, if you want to keep the new version, you need to overwrite the list or save it in a new list.

musical_notes = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
#a
print(musical_notes)
#b
musical_notes = musical_notes[::-1]
print(musical_notes)
#c
musical_notes.reverse()
print(musical_notes)


print('\n-------Ex_2---------')
#2 Print how many times 'do' appears in the list.
print(musical_notes.count('do'))


print('\n-------Ex_3---------')
#3 Given 2 lists, [3, 1, 0, 2] and [6, 5, 4], find 2 ways to merge them into a single list.
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista_new = lista1 + lista2
print(f"The first version of merging is: {lista_new}")

lista1.extend(lista2)
print(f"The second version is : {lista1}")


print('\n-------Ex_4---------')
#4 Sort and display the list generated in the previous exercise. Delete the number 0 from the list using a function and then display the list again.
lista_new.sort()
print(f"The sorted list is: {lista_new}")
lista_new.remove(0)
print(f"The sorted list after deleting number 0 is: {lista_new}")


print('\n-------Ex_5---------')
#5 Using an if statement, check the list generated in exercise 3 and display the following on each branch:
# The list is empty (IF)
# The list is not empty (ELSE)
if len(lista_new) <= 0:
    print('The list is empty')
else:
    print('The list is not empty')


print('\n-------Ex_6---------')
#6 Use a function that empties the list from ex_3.
lista_new.clear()


print('\n-------Ex_7---------')
#7 Rewrite the if statement from exercise 5 and check the result again. Now it should display that the list is empty.
if len(lista_new) <= 0:
    print('The list is empty')
else:
    print('The list is not empty')


print('\n-------Ex_8---------')
#8 Given the dictionary dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}, use a function to display the Students (keys).
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5}
print(dict1.keys())


print('\n-------Ex_9---------')
#9 Print the three students from the above dictionary and their respective grades:
print(f'Ana has the grade: {dict1["Ana"]}')
print(f'Gigel has the grade: {dict1["Gigel"]}')
print(f'Gigel has the grade: {dict1.get("Dorel")}')


print('\n-------Ex_10---------')
#10 Imagine that Dorel has contested his grade and received a 6.
# Modify Dorel's grade to 6
# Print his grade after the modification"
dict1['Dorel'] = 6
print(dict1.get('Dorel'))


print('\n-------Ex_11---------')
#11 Imagine that Gigel is transferring out of class.
# Find a function to remove him
# A new classmate arrives.
# Add Ionica to the dictionary with a grade of 9
# Print the dictionary with the new students.
dict1.pop('Gigel')
print(f"Dict after Gigel's transfer: {dict1}")
dict1['Ionica'] = 9
print(f"Dict after Ionica's transfer: {dict1}")


print('\n-------Ex_12---------')
#12 You have the following sets:
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# Add the day 'luni' to the set zile_sapt
# Display the set zile_sapt
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(f"The set remained the same because duplicate can't be had: {zile_sapt}")


print('\n-------Ex_13---------')
#13 Use an if statement and check if:
# Weekend is a subset of the days of the week
# Weekend is not a subset of the days of the week
if weekend.issubset(zile_sapt):
    print('weekend is a subset of zile_sapt')
else:
    print('weekend is NOT a subset of zile_sapt')


print('\n-------Ex_14---------')
#14 Show the differences between these 2 sets.
diferenta = zile_sapt.difference(weekend)
print(f"The differences between these sets are: {diferenta}")


print('\n-------Ex_15---------')
#15 Display the intersection of elements from these 2 sets:
intersectia = zile_sapt.intersection(weekend)
print(f"The intersection between these 2 sets is: {intersectia}")


print('\n-------BIG ONE---------')
"""
Complex one
"""
# Imagine a football team during a match. Maximum 3 substitutions are allowed.
# Declare a list with 5 players: field_players_list
# Declare a list with 5 substitute players: reserve_players_list
# Declare an empty list for players taken off the field: taken_off_players_list
# substitutions_made = play around with different values to see how data flows through the code
# MAX_SUBSTITUTIONS will be a constant with the value 3
# If player x is on the field and we have more substitutions available then:
# We make the substitution if the player is in the reserve list and not in the field list
# We remove the player taken off from the field list and add him to the taken off list
# We add the player coming in to the field list and remove him from the reserve list
# We print on the screen: x has entered, y has exited. You have z substitutions left (replace x, y and z with your variable names)
# If the player we want to substitute is not on the field:
# Print ‘substitution cannot be made because player x is not on the field’
# Otherwise, print ‘you have z substitutions left’

MAX_SUBSTITUTIONS = 3
substitutions_made = 2
# we calculate the remaining substitutions
remaining_substitutions = MAX_SUBSTITUTIONS - substitutions_made
field_players_list = ['j1', 'j2', 'j3', 'j4', 'j5']
reserve_players_list = ['j6', 'j7', 'j8', 'j9', 'j10']
taken_off_players_list = []
jucator_in = 'j6'
jucator_out = 'j1'

# if the player is in the field and if we still have remaining substitutions
if jucator_out in field_players_list and remaining_substitutions > 0:
    if jucator_in in reserve_players_list and jucator_in not in field_players_list: # we remove the instance in which the player is already in the field
        field_players_list.remove(jucator_out)  # we remove the player
        taken_off_players_list.append(jucator_out)
        field_players_list.append(jucator_in)  # we add a new player
        reserve_players_list.remove(jucator_in)
        remaining_substitutions = remaining_substitutions - 1  # contorizam schimbarea
        print(f'The change was successfully done!')
        print(f'Entered {jucator_in}, Out {jucator_out}, we still have {remaining_substitutions} substitutions left.')
else:
    if remaining_substitutions <= 0:
        print('You are OUT of substitutions.')
    else:
        print(f"We can't make the change because player {jucator_out} is not in the field.")

print(f'After changes, the actual team is {field_players_list}')
print(f"The removed players are: {taken_off_players_list}")

