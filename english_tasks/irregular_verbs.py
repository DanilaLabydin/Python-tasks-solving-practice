#!/usr/bin/python3
##
# create a program that generates a random sentence for english practice
#
import secrets
import csv
import time
import sys

from argparse import ArgumentParser


# create lists to store into them verbs for stat
RIGHT_VERBS = []
WRONG_VERBS = []
FIXED_VERBS = []
RESULT_DICT = {'Correct Verbs': ..., 'Wrong Verbs': ..., 'Fixed Verbs': ...}


def greeting():
    print('This exercise help you learn an irregular english verb!\n'
          'Some rules that you should know\n'
          '    Write only V2 and V3 forms of verb\n'
          '    You have only 2 attempts to write the verb correctly\n'
          'Now enter your name and choose the number of verbs\n')


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
    random_index = secrets.randbelow(len(list_of_verbs) - 1)
    verbs = list_of_verbs[random_index]
    return verbs


def compare_verb(user_input, verb):
    """
    The function compares user's input with certain verb
    :param user_input: a verb that was entered by the user
    :param verb: the current verb(V3 or V3)
    :return: True if the user wrote the correct form, otherwise False
    """
    if user_input.strip().lower() == verb:
        return True

    return False


def display_statistic(name, nb_verb, list1, list2, list3):
    """The function displays all statistic"""
    # compute the rating system and store it into a file
    total = len(RIGHT_VERBS) + len(WRONG_VERBS) + len(FIXED_VERBS)
    scores = ((len(RIGHT_VERBS) + (len(FIXED_VERBS)) * 0.5) / total) * 100
    now_time = time.asctime()

    user_stat = f'{name.title()} | {now_time} | ({nb_verb} verbs) | {scores}%\n'
    with open('results.txt', 'a') as file:
        file.write(user_stat)

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


def generate_attempts(nb_attempt, verb, form_nb):
    for attempt in range(1, nb_attempt + 1):
        print(f'Attempt №{attempt}')
        next_answer = input(f'Enter V{form_nb} again: ')
        if compare_verb(next_answer, verb):
            print('Correct!')
            FIXED_VERBS.append(verb)
            return True
    WRONG_VERBS.append(verb)
    return False


def main():
    # add try except
    arguments = get_args()

    # read the special file to store verbs into a list
    verbs_list = rows_list(arguments.verbs_filename)
    greeting()
    name = input('Enter your name: ')
    nb_verb = int(input('Enter the number of verbs: '))

    if not 0 < nb_verb <= len(verbs_list):
        print('Error! You entered a wrong value (max number is 74)')
        sys.exit(1)

    # ...
    for verb in range(1, nb_verb + 1):
        print(f'\nverb №{verb}')

        # generate and display a random verb from the list and display the V1 of it
        current_verb = random_verb(verbs_list)
        print(current_verb[0])

        # read the answers from the user and compare it with correct v2 and v3 forms
        answer_v2 = input('Enter the V2: ')
        answer_v3 = input('Enter the V3: ')
        result_v2 = compare_verb(answer_v2, current_verb[1])
        result_v3 = compare_verb(answer_v3, current_verb[2])

        # if all answers are correct, display it, save the verb in the list
        # and continue executing with next verb, otherwise give the user
        # 3 attempts to fix it
        if result_v2 and result_v3:
            print('All form is correct!\n')
            RIGHT_VERBS.append(current_verb[0])
            continue

        # check if the v2 is incorrect
        if not result_v2:
            print('\nV2 is wrong!')
            if not generate_attempts(2, current_verb[1], 2):
                print(current_verb[1])

        # check if the v3 is incorrect
        if not result_v3:
            print('\nV3 is wrong!')
            if not generate_attempts(2, current_verb[2], 3):
                print(current_verb[2])

        verbs_list.remove(current_verb)

    # display all statistic and store the result into a file
    display_statistic(name, nb_verb, RIGHT_VERBS, WRONG_VERBS, FIXED_VERBS)


if __name__ == '__main__':
    main()
