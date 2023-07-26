# How can you tell an extrovert from an introvert at NSA?
# Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

# I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
# According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

# For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

# Test examples:

# "EBG13 rknzcyr." -> "ROT13 example."

# "This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"


def rot13(message):
    encoded_message = ""
    for letter in message:
        ord_nb = ord(letter)
        print(ord_nb)
        if 65 <= ord_nb <= 90:
            new_ord = ord_nb - 13
            if new_ord < 65:
                new_ord = 90 + (ord_nb - 65)
            encoded_message += chr(new_ord)
            continue

        if 97 <= ord_nb <= 122:
            new_ord = ord_nb - 13
            if new_ord < 97:
                new_ord = 90 + (ord_nb - 65)
            encoded_message += chr(new_ord)
            continue
        encoded_message += chr(ord_nb)

    return encoded_message


print(rot13("h"))
