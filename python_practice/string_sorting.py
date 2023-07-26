# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
import string
import re


def order(sentence):
    # code here
    order = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
    }

    unsorted_words = sentence.split()
    for unsorted_word in unsorted_words:
        nb = re.findall(r"[1-9]", unsorted_word)
        order[int(str(nb).strip(string.punctuation))] = unsorted_word
    return " ".join([v for v in order.values()]).strip()


while True:
    # value = input('Enter a string [blank line to quit]: ').strip(string.whitespace() + string.punctuation)
    value = "is2 Thi1s T4est 3a"
    if not value:
        break
    else:
        print(order(value))
        break
