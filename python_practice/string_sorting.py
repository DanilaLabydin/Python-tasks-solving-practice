# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
import string
import re

def order(sentence):
  # code here
  order = {}
  unsorted_words = sentence.split()
  for unsorted_word in unsorted_words:
      nb = (re.findall(r'[1-9]', unsorted_word))
      #print(int(nb), type(str(nb)))

      index = str(nb)
      print()
      order[int(index.strip(string.punctuation))] = unsorted_word


  return order





while True:
    #value = input('Enter a string [blank line to quit]: ').strip(string.whitespace() + string.punctuation)
    value = 'is2 Thi1s T4est 3a'
    if not value:
        break
    else:
        print(order(value))
        break
