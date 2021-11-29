#!/usr/bin/python3
##
# create a program that generates a random sentence for english practice
#
import random
import csv
import time
import sys

from argparse import ArgumentParser


# create lists to store into them verbs for stat
RIGHT_VERBS = []
WRONG_VERBS = []
FIXED_VERBS = []


def greeting():
    print('This exercise help you learn an irregular english verb!\n'
          'Some rules that you should know\n'
          '    Write only V2 and V3 forms of verb\n'
          '    You have only 3 attempts to write the verb correctly\n'
          'Now enter your name and choose the number of verb that mean  your level\n'
          '  Dyreniy:        0 < verbs per time <= 10'
          '  Beginner:      11 < verbs per time <= 25\n'
          '  Elementary:    26 < verbs per time <= 40\n'
          '  Master:        41 < verbs per time <= 55\n'
          '  SuperPolya:    56 < verbs per time <= 74\n')


def rows_list(file):
    """
    the function read a file and returns the list of file's rows
    :param file: the current file(name or path)
    :return: the list that contains file's rows in tuple format
    """
    rows = []
    try:
        with open(file) as file:
            # open file like csv file because we want to store each value that is separated by a comma
            csv_file = csv.reader(file)
            for row in csv_file:
                rows.append(row)

            return rows

    except Exception as e:
        print(e)
        exit(1)


def random_verb(list_of_verbs):
    """
    The function creates a random verb from the list
    :param list_of_verbs:
    :return:
    """
    random_index = random.randint(0, len(list_of_verbs) - 1)
    verbs = list_of_verbs[random_index]
    return verbs


def verbs_comparing(verb):
    """
    The function compares user's input with certain verb
    :param verb: the current verb (v1,v2,v3)
    :return: True if the user write the forms correct, otherwise False
    """
    user_answer_v2 = input('Enter V2: ')
    user_answer_v3 = input('Enter V3: ')
    print()
    if user_answer_v2.strip().lower() == verb[0]:
        print('V2 is correct!')
        check_v2 = True
    else:
        print('V2 is not correct!')
        check_v2 = False
    if user_answer_v3.strip().lower() == verb[1]:
        print('V3 is correct!')
        check_v3 = True
    else:
        print('V3 is not correct!')
        check_v3 = False
    print()
    return check_v2 and check_v3


def compare_user_verb(user_input, verb):
    """
    The function compares user's input with certain verb
    :param user_input:
    :param verb: the current verb(V3 and V3)
    :return:
    """
    is_correct = True
    if user_input.strip().lower() == verb[0]:
        print('V2 is correct!')
        return is_correct
    print('V1 is not correct!')
    return False


def display_statistic(name, nb_verb, list1, list2, list3):
    """The function displays all statistic"""
    # compute the rating system and store it into a file
    total = len(right_verbs) + len(wrong_verbs) + len(fixed_verbs)
    scores = ((len(right_verbs) + (len(fixed_verbs)) * 0.5) / total) * 100
    now_time = time.asctime()

    # determine the funny level
    funny_level = ''
    if 0 < nb_verb <= 10:
        funny_level = 'Dyreniy'
    elif 11 < nb_verb <= 25:
        funny_level = 'Beginner'
    elif 26 < nb_verb <= 40:
        funny_level = 'Elementary'
    elif 41 < nb_verb <= 55:
        funny_level = 'Master'
    elif 56 < nb_verb <= 74:
        funny_level = 'SuperPolya'

    string = f'{name.title()} | {now_time} | {funny_level}({nb_verb} verbs) | {scores}%\n'
    with open('results.txt', 'a') as file:
        file.write(string)

    # display lists of verbs
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
    print(f'\nYour scores is {scores}%')


def get_args():
    a = ArgumentParser()
    a.add_argument('-f', '--filename', dest='verbs_filename', type=str, required=True)
    return a.parse_args()


def main():
    # add try except
    arguments = get_args()
    # read the special file to store verbs into a list
    list_of_rows = rows_list(arguments.verbs_filename)
    greeting()
    name = input('Enter your name: ')
    nb_verb = int(input('Enter the number of verbs: '))
    if nb_verb > len(list_of_rows):
        print('Error! You entered a lot of verbs(max number is 74)')
        sys.exit(1)

    for verb in range(1, nb_verb + 1):
        print(f'verb №{verb}')
        # generate a random verb from the list and display the V1
        current_verb = random_verb(list_of_rows)
        print(current_verb[0])

        # compare the input with correct forms and store it in a result
        result = verbs_comparing(current_verb[1:])

        # if the user write verbs wrong, he has only 3 try to write correct, then the verb is added to fixed_verbs list
        # otherwise the program displays all verb's form, add the verb to wrong_verbs list
        if not result:
            for attempt in range(1, 4):
                print(f'Attempt №{attempt}')
                if verbs_comparing(current_verb[1:]):
                    fixed_verbs.append(current_verb[0])
                    break
            else:
                print(current_verb)
                wrong_verbs.append(current_verb[0])
        else:
            right_verbs.append(current_verb[0])
        list_of_rows.remove(current_verb)

    # display all statistic and store the result into a file
    display_statistic(name, nb_verb, right_verbs, wrong_verbs, fixed_verbs)


if __name__ == '__main__':
    main()
