a = [1, 2, 3, [4, 5, 6, [7, 8], 9, 10], 11, 12, [13, 14]]
# a = [3, [4, 5], 6]
b = []


def flat_list(array):
    for i in array:
        print(i)
        if isinstance(i, list):
            flat_list(i)
        else:
            b.append(i)
    return b


flat_list(a)
print()
print(b)
