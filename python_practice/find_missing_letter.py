# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
#You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
#The array will always contain letters in only one case.
import string

def find_missing_letter(chars):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # check the register
    check_register = 0
    if ''.join(chars) == (''.join(chars).upper()):
        check_register = 1
    chars = [char.lower() for char in chars]

    first_letter = alphabet.find(chars[0])
    last_letter = alphabet.find(chars[-1])
    
    #print(first_letter, last_letter)
    #print(alphabet[first_letter:last_letter + 1])

    # find the missing letter
    missing_letter = set(alphabet[first_letter:last_letter + 1]) ^ set(chars)
    letter_format = str(missing_letter).strip(string.punctuation)

    if check_register:
        return letter_format.upper()

    return letter_format


while True:
    #value = input('Enter a string [blank line to quit]: ').strip(string.whitespace() + string.punctuation)
    value2 = ['O','Q','R','S']
    value1 = ['a','b','c','d','f']
    if not value2:
        break
    else:
        print(find_missing_letter(value2))
        break


print(ord('b'))