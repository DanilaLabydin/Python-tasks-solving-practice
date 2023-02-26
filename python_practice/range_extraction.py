#A format for expressing an ordered list of integers is to use a comma separated list of either
#
#   individual integers
#   or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
#
#Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format. 

def solution(nbs_range):
    # your code here
    full_range = [nb for nb in range(nbs_range[0], nbs_range[-1] + 1)]

    # get the diff and sort it
    diff = list(set(nbs_range) ^ set(full_range))
    sort_diff = sorted(diff)
    print(sort_diff)
    print()

    # get diff_nbs's indexes
    diff_nb_location = {diff_nb : full_range.index(diff_nb) for diff_nb in sort_diff}
    diff.sort()
    #print(diff_nb_location)
    #print(full_range)

    output = []
    for nb, index in diff_nb_location.items():
        print(nb, index)
        output.append([nb for nb in range(full_range[0], full_range[index])])
        full_range = full_range[index:]
        print(full_range)
        #print(output)
    return None




test_list = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20] # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
print(solution(test_list))