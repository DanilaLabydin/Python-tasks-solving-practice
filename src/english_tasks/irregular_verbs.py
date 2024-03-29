#!/usr/bin/python3
import random
import csv
import time
import sys
import re

from argparse import ArgumentParser


def greeting():
    print(
        "This exercise help you learn irregular english verbs!\n"
        "Some rules that you should know\n"
        "    Write only V2 and V3 forms of verb\n"
        "    You have only 2 attempts to write the verb correctly\n"
        "Now enter your name and the number of verbs to practice\n"
    )


def get_verbs_list(file):
    """the function read a file and returns the dict of file's verbs"""
    rows = []
    try:
        with open(file) as f:
            # open file like csv file because we want to store each value that is separated by a comma
            csv_f = csv.DictReader(f)
            for row in csv_f:
                rows.append(
                    {
                        "first_form": row["first_form"],
                        "second_form": row["second_form"],
                        "third_form": row["third_form"],
                        "translate": row["translate"],
                    }
                )
            return rows
    except Exception as e:
        print(e)
        exit(1)


def compare_verb(user_input, current_verb):
    """The function compares user's input with certain verb"""
    return user_input.strip().lower() == current_verb


def compute_scores(verb_dict):
    """The function computes the number of user's scores"""
    correct_answers = len(verb_dict["correct"])
    fixed_answers = len(verb_dict["fixed"])
    wrong_answers = len(verb_dict["wrong"])
    if correct_answers + fixed_answers == 0:
        return 0
    total = correct_answers + fixed_answers + wrong_answers
    scores = ((correct_answers + fixed_answers * 0.5) / total) * 100
    return scores


def display_stat(user_name, verb_quantity, verb_dict):
    print("\n\tYOUR STAT")
    print(
        f"Name - {user_name}\n"
        f"Amount of verb - {verb_quantity}\n"
        f"Scores - {compute_scores(verb_dict)}%"
    )
    for key, value in verb_dict.items():
        print(f"{key} - {value}")


def save_statistics(file_name, name, verb_quantity, verb_dict):
    """The function displays all statistics in a given file"""
    user_stat = f"{name.title()} | {time.asctime()} | ({verb_quantity} verbs) | {compute_scores(verb_dict)}%\n"
    with open(file_name, "a") as file:
        file.write(user_stat)


def get_args():
    a = ArgumentParser()
    a.add_argument("-f", "--filename", dest="verbs_filename", type=str, required=True)
    a.add_argument("-o", "--out", dest="stat_filename", type=str, required=False)
    return a.parse_args()


def promt_user(verb):
    """
    The function gives the user 2 attempts to rewrite his answer, if user's new answer is right,
    return True, otherwise False
    """
    for attempt in range(1, 3):
        print(f"Attempt №{attempt}")
        answer = input("Enter again: ")
        if compare_verb(answer, verb):
            print("Correct!")
            return True
        print("Not correct!")
    return False


def generate_reanswer(dict_answers, irregular_verb):
    results = []
    for item in dict_answers.items():
        verb_form, boolean_value = item
        if not boolean_value:
            print(f'\n{verb_form.replace("_", " ").title()} is wrong!')
            results.append(promt_user(irregular_verb[verb_form]))
    return results


def main():
    # get arguments from command line
    arguments = get_args()

    # read the special file to store verbs into a list
    verbs_list = get_verbs_list(arguments.verbs_filename)

    # display the greeting message that contains the rules of the program
    greeting()
    user_name = input("Enter your name: ")

    while True:
        verb_quantity = int(input("Enter the number of verb to practice: "))
        if not 0 < verb_quantity <= 74:
            print("Error! You entered a wrong value (max number is 74)")
            sys.exit(1)

        # mix the content of a list
        random.shuffle(verbs_list)

        # extract the certain number of verb to the sub_verbs_list from the main list
        sample_verbs = verbs_list[:verb_quantity]

        # create a dict to store each verb in the separated group (correct; wrong;fixed) verbs
        user_output = {"correct": [], "wrong": [], "fixed": []}

        # display the message how to exit the program
        print("\nEnter 'q' to quit!\n")

        for count, verb in enumerate(sample_verbs, start=1):
            print(f"\nThe verb №{count}\n")
            print(f'{verb["first_form"]} - {verb["translate"]}')

            # read the answers from the user and compare it with correct v2 and v3 forms and store them
            user_answers = input(
                "Enter the V2 and V3 separated by commas format[did done]: "
            )
            if user_answers == "q":
                break

            try:
                values = re.search(r"^\s*([A-Za-z]*)\s*([A-Za-z]*)$", user_answers)

                # store the answers in special dictionary
                result_answers = {
                    "second_form": compare_verb(values.group(1), verb["second_form"]),
                    "third_form": compare_verb(values.group(2), verb["third_form"]),
                }
            except AttributeError:
                print("\nYour answer was entered in the wrong format!")
                continue

            # if all answers are right, add the verb into a sorted group and go to the next irregular verb
            if all(result_answers.values()):
                user_output["correct"].append(verb["first_form"])
                print("All forms are correct!")
                continue

            # give to the user two attempts to rewrite the answer. If the reanswer is correct, add the verb
            # into a fixed group, otherwise into a wrong group
            if all(generate_reanswer(result_answers, verb)):
                user_output["fixed"].append(verb["first_form"])
                continue
            user_output["wrong"].append(verb["first_form"])
            print(f'\nCorrect forms: {verb["second_form"]}, {verb["third_form"]}')

        # display the practice results
        display_stat(user_name, verb_quantity, user_output)

        # if user entered the save file, then save info in it
        if arguments.stat_filename:
            save_statistics(
                arguments.stat_filename, user_name, verb_quantity, user_output
            )

        # ask the user about next practice
        ask_again = input("Do you want to complete this task again(q to quit): ")
        if ask_again == "q":
            break


if __name__ == "__main__":
    main()
