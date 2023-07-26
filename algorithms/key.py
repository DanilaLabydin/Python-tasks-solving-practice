# key_quantity = int(input())
# key_values = list(map(int, input().split()))
# key_positions = list(map(int, input().split()))
# len_word = int(input())
# word_letters = list(map(int, input().split()))


# transition_quantities = 0
# prev_position = 0
# for i in range(len(word_letters)):

#     current_key_index = key_values.index(word_letters[i])
#     current_position = key_positions[current_key_index]

#     if i == 0:
#         prev_position = current_position
#         continue

#     if current_position == prev_position:
#         continue

#     prev_position = current_position
#     transition_quantities += 1

# print(transition_quantities)


N = int(input())
key_identifiers = list(map(int, input().split()))
row_numbers = list(map(int, input().split()))
K = int(input())
abstract_characters = list(map(int, input().split()))

row_dict = {}
for i in range(N):
    row_dict[key_identifiers[i]] = row_numbers[i]

multi_row = 0
prev_row = row_dict[abstract_characters[0]]

for i in range(1, K):
    curr_row = row_dict[abstract_characters[i]]
    if curr_row != prev_row:
        multi_row += 1
    prev_row = curr_row

print(multi_row)
