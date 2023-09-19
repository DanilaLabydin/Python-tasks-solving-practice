def is_palindrome(num):
    if num // 10 == 0:
        return False

    temp = num
    reversed_num = 0
    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp //= 10

    return num == reversed_num


def infinite_palindrome():
    num = 0
    while True:
        if is_palindrome(num):
            i = yield num
            if i is not None:
                num = i

        num += 1


pal_gen = infinite_palindrome()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    pal_gen.send(10 ** (digits))
