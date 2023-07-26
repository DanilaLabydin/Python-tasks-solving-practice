# first_row = list(map(int, input().split()))
# sculptures_ice = list(map(int, input().split()))


# skulpture_quantity = first_row[0]
# perfect_ice = first_row[1]
# all_time = first_row[2]


# perfect_sculpture_list = []
# perfect_sculpture_nbs = 0

# # print('----------------------------------------------------------------')

# ice_to_perfect = []
# for i in range(len(sculptures_ice)):
#     ice_to_perfect.append(abs(perfect_ice - sculptures_ice[i]))


# skulp_dict = {}
# for i in range(len(sculptures_ice)):
#     skulp_dict[ice_to_perfect[i]] = sculptures_ice[i]


# # print(skulp_dict)
# # print()

# ice_to_perfect.sort()
# # print(ice_to_perfect)
# # print()


# for i in range(len(ice_to_perfect)):
#     all_time -= ice_to_perfect[i]

#     if all_time < 0:
#         continue

#     perfect_sculpture_nbs += 1


#     inital_ice = skulp_dict[ice_to_perfect[i]]
#     initial_ice_index = sculptures_ice.index(inital_ice)
#     perfect_sculpture_list.append(initial_ice_index + 1)
#     # del sculptures_ice[initial_ice_index]


# print(perfect_sculpture_nbs)
# perfect_sculpture_list_str = " ".join(map(str, perfect_sculpture_list))
# print(perfect_sculpture_list_str)


def find_ideal_sculptures(N, X, T, sculptures):
    sculpture_list = [(i, abs(weight - X)) for i, weight in enumerate(sculptures, 1)]

    sorted_sculptures = sorted(sculpture_list, key=lambda x: x[1])

    ideal_sculptures = []
    remaining_time = T

    for sculpture in sorted_sculptures:
        index, difference = sculpture

        if difference <= remaining_time:
            ideal_sculptures.append(index)
            remaining_time -= difference

        else:
            break

    return len(ideal_sculptures), ideal_sculptures


N, X, T = map(int, input().split())
sculptures = list(map(int, input().split()))


k, ideal_sculptures = find_ideal_sculptures(N, X, T, sculptures)


print(k)
print(*ideal_sculptures)
