card_nums = int(input())
jo_seq = input().split()
win_seq = input().split()


def get_answer(card_nums, jo_seq, win_seq):
    answer = "NO"
    for i in range(card_nums):
        jo_num = int(jo_seq[i])
        win_num = int(win_seq[i])

        if jo_num == win_num:
            continue

        k = i + 2

        # if k >= card_nums:
        #     print('dfsf ')
        #     return "NO"
        # print(f'i: {i} - k:{k}')
        for k in range(card_nums):
            jo_seq_copy = jo_seq.copy()

            first_part = jo_seq_copy[:i]
            second_part = jo_seq_copy[i:k]
            last_part = jo_seq_copy[k:]

            # print(f'first: {first_part} - second: {second_part} - last: {last_part}')
            second_part.sort()
            if first_part + second_part + last_part == win_seq:
                return "YES"

        return "NO"
    return answer


if len(jo_seq) != len(win_seq):
    print("NO")

if jo_seq == win_seq:
    print("YES")
else:
    print(get_answer(card_nums, jo_seq, win_seq))




