#!/usr/bin/env python3
##
# write a function, that remove outliers from the list of values and a main program to show it
#


def remove_outliers(data, num):
    """
    the function removes outliers from the list
    :param data: the list of values
    :param num: the number of n largest and n smallest element in a list
    :return: the new copy of list(sorted order) without outliers
    """
    new_data = sorted(data)
    for i in range(num):
        del new_data[0]
        del new_data[-1]
    return new_data


def main():
    data = []
    num = int(input("Enter the number(0 to quit): "))

    while num != 0:
        data.append(num)
        num = int(input("Enter the number(0 to quit): "))
    nb_outliers = int(
        input("Enter the number of outliers that will bw removed from the list: ")
    )

    if nb_outliers * 2 < len(data):
        new_data = remove_outliers(data, nb_outliers)
        print(f"\nThe original list is: {data}")
        print(f"The list without outliers is: {new_data}")
    else:
        print("ERROR! you wrote not enough values for the calculations")


if __name__ == "__main__":
    main()
