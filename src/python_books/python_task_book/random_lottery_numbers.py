#!/usr/bin/env python3
##
# write a program that generates a random selection of 6 numbers(between 1 and 49)
# for a lottery ticket,ensure that the 6 numbers selected do not contains duplicates
#
import random

MIN_LIMIT = 1
MAX_LIMIT = 49
DIGITS_IN_TICKET = 6

ticket_numbers = []

# create a loop while the selection of numbers is not equal to 6
while len(ticket_numbers) != DIGITS_IN_TICKET:
    nb = random.randint(MIN_LIMIT, MAX_LIMIT)

    # add a number only if it isn't in selection
    if nb not in ticket_numbers:
        ticket_numbers.append(nb)

# display the result
ticket_numbers.sort()
print(f"Your numbers are: ", end="")
for nb in ticket_numbers:
    print(nb, end=" ")
print()
