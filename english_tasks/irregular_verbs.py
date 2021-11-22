#!/usr/bin/python3
##
# create a program that generates a random sentence for english practice
#
import random
import csv

# create lists to store into them verbs for statstic
right_verbs = []
wrong_verbs = []
fixed_verbs = []


def rows_list(file):
    """
    the function read a file and returns the list of file's rows
    :param file: the current file(name or path)
    :return: the list that contains file's rows in tuple format
    """
    rows = []
    with open(file) as file:
        # open file like csv file because we want to store each value that is separated by a comma
        csv_file = csv.reader(file)
        for row in csv_file:
            rows.append(row)
    return rows


def random_verb(list_of_verbs):
    """
    The function creates a random verb from the list
    :param list_of_verbs:
    :return:
    """
    random_index = random.randint(0, len(list_of_verbs) - 1)
    verbs = list_of_verbs[random_index]
    return verbs


def verbs_comparing(user_input, verb):
    """
    The function compares user's input with a certain verb
    :param user_input: v2 and v3 forms of verb that was entered by the user
    :param verb: v2 and v3 forms of a certain verb
    :return:
    """
    # delete first form from comparing and init a variable to check whether comparing is correct
    total = 0
    print()
    for i in range(2):
        if user_input[i].strip() == verb[i]:
            total += 1
            print(f'V{i+1} is correct!')
        else:
            print(f'V{i+1} is incorrect!')
    print()
    # if the user write wrong form, return False, otherwise True
    if total != 2:
        return False
    else:
        return True


def display_statistic(list1, list2, list3):
    print()
    print(f'Correct verbs: ', end="")
    for i in list1:
        print(i, end=",")
    print()
    print(f'Wrong verbs:   ', end="")
    for i in list2:
        print(i, end=",")
    print()
    print(f'Fixed verbs:   ', end="")
    for i in list3:
        print(i, end=",")


def main():
    list_of_rows = rows_list('irregular_verbs')
    while len(list_of_rows) != 0:
        current_verb = random_verb(list_of_rows)
        print(current_verb[0])
        user_answer = input('Enter here: ')
        if user_answer == "q":
            break
        user_verbs = user_answer.split()

        # check every word from user's input(you should def a function later)
        result = verbs_comparing(user_verbs, current_verb[1:])

        if not result:
            wrong_verbs.append(current_verb[0])
            ask_hint = input('Do you want to get a hint?(yes/no): ')
            if ask_hint.lower() == 'yes':
                print(current_verb)
            next_try = input('Do you want to do it again? (yes/no): ')
            while next_try != 'no':
                user_answer = input('Enter here: ')
                user_verbs = user_answer.split()
                result = verbs_comparing(user_verbs, current_verb[1:])
                if result:
                    fixed_verbs.append(current_verb[0])
                    wrong_verbs.remove(current_verb[0])
                    break
                else:
                    next_try = input('Do you want to do it again? (yes/no): ')

        else:
            right_verbs.append(current_verb[0])
        list_of_rows.remove(current_verb)
    ask_stat = input('Do you want to see a statistic?(yes/no): ')
    if ask_stat == 'yes':
        display_statistic(right_verbs, wrong_verbs, fixed_verbs)


if __name__ == '__main__':
    main()

# подсказка на первый раз каждый раз
# только yes и no
# добавить перевод



