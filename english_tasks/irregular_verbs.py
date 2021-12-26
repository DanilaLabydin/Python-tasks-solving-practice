#!/usr/bin/python3
import random
import csv
import time
import sys

from argparse import ArgumentParser


def greeting():
    print('This exercise help you learn irregular english verbs!\n'
          'Some rules that you should know\n'
          '    Write only V2 and V3 forms of verb\n'
          '    You have only 2 attempts to write the verb correctly\n'
          'Now enter the number of verbs to practice\n')


def get_verbs_list(file):
    """the function read a file and returns the list of file's rows"""
    rows = []

    try:
        with open(file) as f:
            # open file like csv file because we want to store each value that is separated by a comma

            csv_f = csv.DictReader(f)
            for row in csv_f:
                rows.append([row['first_form'], row['second_form'],
                             row['third_form'], row['translate']])

            return rows

    except Exception as e:
        print(e)
        exit(1)


def compare_verb(user_input, current_verb):
    """The function compares user's input with certain verb"""
    if user_input.strip().lower() == current_verb:
        return True
    return False


def compute_scores(verb_dict):
    """The function computes the number of user's scores"""
    correct_answers = len(verb_dict['correct'])
    fixed_answers = len(verb_dict['fixed'])
    wrong_answers = len(verb_dict['wrong'])
    total = correct_answers + fixed_answers + wrong_answers
    scores = ((correct_answers + fixed_answers * 0.5) / total) * 100
    return scores


def display_stat(user_name, verb_quantity, verb_dict):
    print('\n\tYOUR STAT')
    print(f'Name - {user_name}\n'
          f'Amount of verb - {verb_quantity}\n'
          f'Scores - {compute_scores(verb_dict)}%')
    for key, value in verb_dict.items():
        print(f'{key} - {value}')


def save_statistics(file_name, name, verb_quantity, verb_dict):
    """The function displays all statistics in a given file"""
    user_stat = f'{name.title()} | {time.asctime()} | ({verb_quantity} verbs) | {compute_scores(verb_dict)}%\n'
    with open(file_name, 'a') as file:
        file.write(user_stat)


def get_args():
    a = ArgumentParser()
    a.add_argument('-f', '--filename', dest='verbs_filename', type=str, required=True)
    a.add_argument('-o', '--out', dest='stat_filename', type=str, required=False)
    return a.parse_args()


def generate_attempts(nb_attempt, verb):
    """
    The function gives the user a certain number of attempts to rewrite his answer, if user's new answer is right,
    return True, otherwise False
    """
    for attempt in range(1, nb_attempt + 1):
        print(f'Attempt №{attempt}')
        next_answer = input('Enter: ')
        if compare_verb(next_answer, verb):
            print('Correct!')
            return True
    return False


def generate_sub_verbslist(verbs_list, item_quantity):
    """The function generates a list from part of an other list"""
    sub_list = verbs_list[:item_quantity]
    return sub_list


def main():
    # get arguments from command line
    arguments = get_args()

    # read the special file to store verbs into a list
    verbs_list = get_verbs_list(arguments.verbs_filename)

    # display the greeting message that contains the rules of the program
    greeting()
    user_name = input('Enter your name: ')

    while True:
        verb_quantity = int(input('Enter the number of verb to practice: '))
        if not 0 < verb_quantity <= 75:
            print('Error! You entered a wrong value (max number is 75)')
            sys.exit(1)

        # mix the content of a list
        random.shuffle(verbs_list)

        # extract the certain number of verb to the sub_verbs_list from the main list
        sample_verbs = generate_sub_verbslist(verbs_list, verb_quantity)

        # create a dict to store each verb in the separated group (correct; wrong;fixed) verbs
        sorted_verbs = {'correct': [], 'wrong': [], 'fixed': []}

        # iterate each verb in the list and display the number of iteration
        count = 0

        for verb in sample_verbs:
            count += 1
            print(f'\nThe verb №{count}\n')
            print(f'{verb[0]} - {verb[3]}')

            # read the answers from the user and compare it with correct v2 and v3 forms
            answer_v2 = input('Enter the V2: ')
            answer_v3 = input('Enter the V3: ')
            result_v2 = compare_verb(answer_v2, verb[1])
            result_v3 = compare_verb(answer_v3, verb[2])

            # if all answers are right, store infinitive with appropriate key and continue iterating,
            # otherwise give two attempts to user to rewrite their answers

            if result_v2 and result_v3:
                sorted_verbs['correct'].append(verb[0])
                print('All forms are correct!')
                continue

            # create a variable to store the result of rewriting, and give the chance to rewrite if the answer is wrong
            second_chance = []
            if not result_v2:
                print('\nV2 is wrong!')
                second_chance.append(generate_attempts(2, verb[1]))

            if not result_v3:
                print('\nV3 is wrong!')
                second_chance.append(generate_attempts(2, verb[2]))

            # if all attempts are right, then add the verb into a fixed group, otherwise add into a wrong group

            if all(second_chance):
                sorted_verbs['fixed'].append(verb[0])
                continue

            sorted_verbs['wrong'].append(verb[0])
            print(f'Correct forms: {verb[1]}, {verb[2]}\n')

        # display the practice results
        display_stat(user_name, verb_quantity, sorted_verbs)

        # if user entered the save file, then save info in it
        if arguments.stat_filename:
            save_statistics(arguments.stat_filename, user_name, verb_quantity, sorted_verbs)

        # ask the user about next practice
        ask_again = input('Do you want to complete this task again(q to quit): ')
        if ask_again == 'q':
            break


if __name__ == '__main__':
    main()
    