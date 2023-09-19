# Write a function to split a string and convert it into an array of words.


def string_to_array(s):
    if len(s) == 0:
        return [""]
    return s.split()


string = input("Enter a string: ")
print(string_to_array(string))
