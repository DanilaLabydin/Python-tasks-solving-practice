import random


def quiq_sort(array):
    if len(array) < 2:
        return array

    random_index = random.randint(0, len(array) - 1)
    pivot = array.pop(random_index)
    less = [i for i in array if i < pivot]
    greater = [i for i in array if i > pivot]
    return quiq_sort(less) + [pivot] + quiq_sort(greater)


print(quiq_sort([10, 5, 2, 3]))
