#!/usr/bin/env python3
##
# the n number is perfect only if the sum of all proper divisors of n is equal to n
# write a function that determine whether or not a positive number is perfect
# write a main program that uses this function to identify and display all of the perfect
# numbers between 1 and 10_000
#
from list_of_proper_divisors import proper_divisor

LIMIT = 10_000


def is_number_perfect(nb):
    """
    The function determines whether the number a perfect or not
    :param nb: a number that was entered by the user
    :return: True if number is perfect, otherwise False
    """
    # compute the list of divisors
    list_of_divisors = proper_divisor(nb)

    # compute the sum of divisors and determine whether the number is perfect
    total = 0
    for num in list_of_divisors:
        total += num
    if total == nb:
        return True
    return False


def main():
    print(f"The number perfect number between 1 and {LIMIT} is: ")
    for i in range(1, LIMIT + 1):
        if is_number_perfect(i):
            print(i)


if __name__ == "__main__":
    main()
