def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


def multi_yield():
    a = 0
    yield f"Now a is {a}"
    a += 1
    yield f"Now a is {a}"
    a += 1
    yield f"Now a is {a}"
    a += 1
    yield f"Now a is {a}"
    a += 1
    yield f"Now a is {a}"
    a += 1


def is_palindrome(num):
    if num // 10 == 0:
        return False

    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp //= 10
        # print(f'reversed_num: {reversed_num} - temp: {temp}')

    return num == reversed_num


def infinite_palindrome():
    num = 0
    while True:
        if is_palindrome(num):
            i = yield num
            if i is not None:
                num = i
        num += 1


seq = infinite_sequence()
print(seq)

print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))

test = ({x: x} for x in range(10))
print(test)
print(next(test))
print(next(test))

test2 = multi_yield()
print(next(test2))
print(next(test2))

print(is_palindrome(33))
print()
test3 = infinite_palindrome()
print(next(test3))
print(next(test3))
