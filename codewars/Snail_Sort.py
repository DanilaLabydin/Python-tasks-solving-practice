# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]

# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]


def snail(snail_map):
    new_list = []
    while len(snail_map) >= 1:
        new_list += snail_map[0]
        del snail_map[0]
        for i in snail_map:
            new_list.append(i.pop(-1))

        snail_map = snail_map[::-1]
        for i in range(len(snail_map)):
            snail_map[i] = snail_map[i][::-1]

    return new_list
