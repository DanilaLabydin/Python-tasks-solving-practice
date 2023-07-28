def Merge(A, p, q, r):
    # get left and right parst
    left_array = A[p:q]
    right_array = A[q:r]

    # iterate over parts and compare their elements, k - index for merged array
    i = 0
    j = 0
    k = 0
    while i < len(A[p:q]) and j < len(right_array):
        # replace smaller item
        if left_array[i] < right_array[j]:
            A[p + k] = left_array[i]
            i += 1
        else:
            A[p + k] = right_array[j]
            j += 1

        k += 1

    # if there are items after iterating just add them to the merged array
    while i < len(left_array):
        A[p + k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        A[p + k] = right_array[j]
        j += 1
        k += 1


def Sort(A, p, r):
    # base case: array (A[p:r]) contains only one element
    if abs(p - r) == 1:
        return

    # get a middle and sort left and right array's parts and merge to sort them
    q = (p + r) // 2
    Sort(A, p, q)
    Sort(A, q, r)
    Merge(A, p, q, r)


# def sort2(array):
#     if len(array) == 1:
#         return

#     left_array = array[:len(array) // 2]
#     right_array = array[len(array) // 2:]
#     sort(left_array)
#     sort(right_array)

#     i = 0
#     j = 0
#     k = 0
#     while i < len(left_array) and j < len(right_array):
#         if left_array[i] < right_array[j]:
#             array[k] = left_array[i]
#             i += 1

#         else:
#             array[k] = right_array[j]
#             j += 1

#         k += 1
#     while i < len(left_array):
#         array[k] = left_array[i]
#         i += 1
#         k += 1

#     while j < len(right_array):
#         array[k] = right_array[j]
#         j += 1
#         k += 1


unsorted = [5, 2, 4, 6, 1, 3, 2, 6]
Sort(unsorted, 0, len(unsorted))
print(unsorted)
