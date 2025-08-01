# -*- coding: utf-8 -*-
"""Day 10 lab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QgnnexJChmHfM5ELGCUiEKm8jsG9Fb5v
"""

#Q1) Write a Python program to sum all the items in a list.
# Python program to sum all the items in a list using list method

numbers = [20,25,30,35,40,]
total = sum(numbers)
print("The sum of all items in the list is:", total)

#Q2)Write a Python program to get the largest and smallest number from a list without builtin functions.

numbers = [23, 1, 89, 17, 56, 3, 98, 45]
smallest = numbers[0]
largest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
print("Smallest number in the list is:", smallest)
print("Largest number in the list is:", largest)

#Q3)Write a Python program to find duplicate values from a list and display those.

numbers = [4, 7, 2, 7, 3, 4, 9, 1, 3, 8, 2, 6]
duplicates = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])
if duplicates:
    print("Duplicate values in the list are:", duplicates)
else:
    print("No duplicates found.")

#Q4)Write a Python program to split a given list into two parts where the length of the first part of the list is given.

original_list = [10, 20, 30, 40, 50, 60, 70, 80]
first_part_length = 5
if 0 <= first_part_length <= len(original_list):
    first_part = []
    second_part = []

    for i in range(len(original_list)):
        if i < first_part_length:
            first_part.append(original_list[i])
        else:
            second_part.append(original_list[i])
    print("Original List:", original_list)
    print("First Part:", first_part)
    print("Second Part:", second_part)
else:
    print("Invalid length for first part.")

#Q5)Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
#Original list:
#['red', 'green', 'white', 'black']
#Traverse the said list in reverse order:
#black
#white
#green
#red

colors = ['red', 'green', 'white', 'black']

print("Original list:")
print(colors)
print("\nTraverse the list in reverse order with original indices:\n")
for i in range(len(colors) - 1, -1, -1):
    print(f"{colors[i]} (original index: {i})")