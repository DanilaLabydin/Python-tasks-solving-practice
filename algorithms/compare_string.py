string_nb = int(input())
strings_list = [str(input()) for _ in range(2 * string_nb)]

# print()
# print(string_nb)
# print(strings_list)


def check_strings(s1, s2):
    if len(s1) != len(s2):
        return "NO"
    s1_dict = {}
    s2_dict = {}

    for i in range(len(s1)):
        if s1_dict.setdefault(s1[i], s2[i]) != s2[i]:
            return "NO"

        if s2_dict.setdefault(s2[i], s1[i]) != s1[i]:
            return "NO"

    return "YES"


s1_list = strings_list[::2]
s2_list = strings_list[1::2]


for i in range(len(s1_list)):
    # if len(s1_list[i]) != len(s2_list[i]):
    #     print("NO")
    # elif len(set(s1_list[i])) == len(set(s2_list[i])):
    #     print("YES")
    # else:
    #     print("NO")
    print(check_strings(s1_list[i], s2_list[i]))

# print(s1_list)
# print(s2_list)
