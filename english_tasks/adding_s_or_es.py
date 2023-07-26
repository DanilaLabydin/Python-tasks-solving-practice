import re

verbs = ["swim", "read", "teach", "sex", "kiss", "fish"]


def add_ending(word):
    """
    The function add the ending to the vern by english grammar
    :param word: the V1 verb
    :return: the V1 with right ending
    """
    if re.search(r"ss|ch|sh|x", word):
        return word + "es"
    return word + "s"


def main():
    for verb in verbs:
        print(add_ending(verb))


if __name__ == "__main__":
    main()
