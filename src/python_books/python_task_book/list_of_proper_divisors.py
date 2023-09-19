#!/usr/bin/env python3
##
# write a function, that computes all of the proper divisors of a positive integer
#


def proper_divisor(n):
    """
    The function computes all of the proper divisors and stores them in a list
    :param n: a positive integer
    :return: the list of proper divisors
    """
    proper_divisors = []
    divisor = 1
    while divisor != n:
        if n % divisor == 0:
            proper_divisors.append(divisor)
        divisor += 1
    return proper_divisors


def main():
    nb = int(input("Enter the number: "))
    print(f"The proper divisors of this number is: {proper_divisor(nb)}")


if __name__ == "__main__":
    main()
