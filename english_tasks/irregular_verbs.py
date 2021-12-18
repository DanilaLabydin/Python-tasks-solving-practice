#!/usr/bin/python3
##
# create a program that generates a random sentence for english practice
#
import re
import random
import csv
import time
import sys

from argparse import ArgumentParser


# create lists to store into them verbs for stat
RESULT_DICT = {'correct_verbs': [], 'wrong_verbs': [], 'fixed_verbs': []}


def greeting():
    print('This exercise help you learn irregular english verbs!\n'
          'Some rules that you should know\n'
          '    Write only V2 and V3 forms of verb\n'
          '    You have only 2 attempts to write the verb correctly\n'
          'Now enter the number of verbs\n')


def get_verbs_list(file):
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


def random_verb(list_of_verbs: list):
    """
    The function creates a random verb from the list
    :param list_of_verbs:
    :return:
    """
    random_index = random.randint(0, len(list_of_verbs) - 1)
    verbs = list_of_verbs[random_index]
    return verbs


def compare_verb(user_input: str, current_verb: str):
    """
    The function compares user's input with certain verb
    :param user_input: a verb that was entered by the user
    :param current_verb: the current verb(V3 or V3)
    :return: True if the user wrote the correct form, otherwise False
    """
    pattern = current_verb
    result = re.search(pattern, user_input)
    if result is None:
        return False

    return True


def display_statistic(file_name, name, verb_quantity, verb_dict):
    """The function displays all statistic"""
    # compute the rating system and store it into a file
    total = 0
    correct_answers = len(verb_dict['correct_verbs'])
    fixed_answers = len(verb_dict['fixed_verbs'])
    for key, value in verb_dict.items():
        total += len(value)

    scores = ((correct_answers + fixed_answers * 0.5) / total) * 100
    now_time = time.asctime()

    user_stat = f'{name.title()} | {now_time} | ({verb_quantity} verbs) | {scores}%\n'
    with open(file_name, 'a') as file:
        file.write(user_stat)

    # display lists of verbs
    for key, value in RESULT_DICT.items():
        print(f'{key} - {value}')


def get_args():
    a = ArgumentParser()
    a.add_argument('-f', '--filename', dest='verbs_filename', type=str, required=True)
    a.add_argument('-o', '--name', dest='stat_filename', type=str, required=True)
    return a.parse_args()


def generate_attempts(nb_attempt, verb, form_nb):
    for attempt in range(1, nb_attempt + 1):
        print(f'Attempt №{attempt}')
        next_answer = input(f'Enter V{form_nb} again: ')
        if compare_verb(next_answer, verb):
            print('Correct!')
            RESULT_DICT['fixed_verbs'].append(verb)
            return True
    RESULT_DICT['wrong_verbs'].append(verb)
    return False


def check_answers(irregular_verb, result_v2, result_v3):
    """
    Check if the answers are correct, if all answers are correct, store the infinitive of verb in dictionary(correct_v)
    otherwise give the user attempts to write the answer correctly
    """
    if result_v2 and result_v3:
        print('All form is correct!\n')
        RESULT_DICT['correct_verbs'].append(irregular_verb[0])
        return

    # check if the v2 is incorrect
    if not result_v2:
        print('\nV2 is wrong!')
        if not generate_attempts(2, irregular_verb[1], 2):
            print(f'The correct form - {irregular_verb[1]}')

    # check if the v3 is incorrect
    if not result_v3:
        print('\nV3 is wrong!')
        if not generate_attempts(2, irregular_verb[2], 3):
            print(f'The correct form - {irregular_verb[2]}')
    return


def main():
    arguments = get_args()

    # read the special file to store verbs into a list
    verbs_list = get_verbs_list(arguments.verbs_filename)
    greeting()
    name = input('Enter your name: ')
    nb_verb = int(input('Enter the number of verbs: '))

    if not 0 < nb_verb <= len(verbs_list):
        print('Error! You entered a wrong value (max number is 74)')
        print(len(verbs_list))
        sys.exit(1)

    for verb in range(1, nb_verb + 1):
        print(f'\nverb №{verb}')
        current_verb = random_verb(verbs_list)
        print(current_verb[0])

        # read the answers from the user and compare it with correct v2 and v3 forms
        answer_v2 = input('Enter the V2: ')
        answer_v3 = input('Enter the V3: ')
        result_v2 = compare_verb(answer_v2, current_verb[1])
        result_v3 = compare_verb(answer_v3, current_verb[2])

        # check the answers and delete the verb from the list
        check_answers(current_verb, result_v2, result_v3)
        verbs_list.remove(current_verb)

    # display all statistic and store the result into a file
    display_statistic(arguments.stat_filename, name, nb_verb, RESULT_DICT)


if __name__ == '__main__':
    main()
