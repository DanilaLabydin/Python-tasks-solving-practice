##
# create a program that reads words from the user and stores them into a list
# removing all duplicates
#

words = []
words_without_duplicates = []
# read the dimension from the user("" to quit)
while True:
    word = input(f'Enter the word to store it into a list(blank line to quit): ')
    if word == "":
        break
    words.append(word)

# add each word into a list only if it hasn't been already in it
for word in words:
    if word not in words_without_duplicates:
        words_without_duplicates.append(word)

# display the result(each word has it's own line)
for word in words_without_duplicates:
    print(word)
print(f"That's it my friend")
