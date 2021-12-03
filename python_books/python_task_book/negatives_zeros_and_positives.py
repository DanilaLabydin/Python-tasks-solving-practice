#!/usr/bin/env python3
##
# create a program that reads integer from the user until a blank line is entered, then
# the program should display all of the negative numbers, followed by all of the zeros,
# followed by all of he positive numbers. All the numbers should be displayed in the same order
# that they were entered by the user
#
import sys

numbers = []
while True:
    nb = input('Enter the number(blank line to quit): ')
    if nb == "":
        break
    numbers.append(nb)

# check if all elements are not a alpha
for element in numbers:
    if element.isalpha():
        print(f"ERROR! there is a non-numeric in your list!")
        sys.exit(1)

# store all the numbers into three lists for its nature(negatives, zeros, positives)
negatives = []
zeros = []
positives = []
for number in numbers:
    if int(number) < 0:
        negatives.append(number)
    elif int(number) > 0:
        positives.append(number)
    else:
        zeros.append(number)

# display the result
print('The sorted number is: ')
for nb in negatives:
    print(nb, end=", ")
for nb in zeros:
    print(nb, end=", ")
for nb in positives:
    print(nb, end=", ")
