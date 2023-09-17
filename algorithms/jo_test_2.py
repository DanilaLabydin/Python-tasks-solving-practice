s = input()


def get_count(letter_dict, word):
    count = 0
    while True:
        for letter in word:
            if letter not in letter_dict:
                return count
            
            if letter_dict[letter] == 0:
                return count

            letter_dict[letter] -= 1
        count += 1


word = "sheriff"
letter_dict = {}
for letter in s:
    if letter not in word:
        continue

    if letter not in letter_dict:
        letter_dict[letter] = 1
    else:
        letter_dict[letter] += 1


print(get_count(letter_dict, word))