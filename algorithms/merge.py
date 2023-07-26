def merge(A, p, q, r):
    left_array = A[p:q]
    right_array = A[q:r]
    # print(f'left_array: {left_array} --- right_array: {right_array} --- p:{p} --- q:{q} --- r:{r} ')
    i = 0
    j = 0
    k = 0
    while i < len(A[p:q]) and j < len(right_array):
        if left_array[i] < right_array[j]:
            A[p + k] = left_array[i]
            i += 1

        else:
            A[p + k] = right_array[j]
            j += 1

        k += 1
    while i < len(left_array):
        A[p + k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        A[p + k] = right_array[j]
        j += 1
        k += 1
    # print(A)


def sort2(A, p, r):
    if p < r and abs(p - r) != 1:
        q = (p + r) // 2
        # print(f'p: {p} - r: {r} - q: {q} --- {A[p:r]}')
        sort2(A, p, q)
        sort2(A, q, r)
        merge(A, p, q, r)


# def sort(array):
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
            


# def Merge(A, p, q, r):
#     left_part = A[p:q]
#     right_part = A[q:r]

#     i = 0
#     k = 0
#     temp_list = []
#     while i < q and k < r - 1:
#         if left_part[i] < right_part[k]:
#             temp_list.append(left_part[i])
#             i += 1

#         else:
#             temp_list.append(right_part[k])
#             k += 1
            
#     while i != q:
#         temp_list.append(left_part[i])
#         i += 1

#     while k != r:
#         temp_list.append(right_part[k])
#         k += 1

#     for i in range(len(A)):
#         A[i] = temp_list[i]


# def Sort(A, p, r):
#     print(f'p: {p} - r: {r}')
#     if p == r:
#         return
    
#     q = (p + r) // 2
#     Sort(A, p, q)
#     Sort(A, q, r)
#     Merge(A, p, q, r)


unsorted = [5,2,4,6,1,3,2,6]
sort2(unsorted, 0, len(unsorted))
print(unsorted)

# print(Sort(unsorted, 0, len(unsorted)))