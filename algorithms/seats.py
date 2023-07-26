import re


REQUIREMENTS = {
    "left": False,
    "right": True,
}


def decode_group_map(group):
    pattern = re.findall(r"^([0-9]*) (left|right) (aisle|window)", group)
    group = pattern[0]
    num = group[0]
    side = group[1]
    position = group[2]
    return num, side, position


def check_group_requirements(row, side, position, pass_aisle, free_row_indexes):
    if (side == "left" and pass_aisle is True) or (
        side == "right" and pass_aisle is False
    ):
        return False

    if position == "window":
        for i in free_row_indexes:
            if i == 0 or i == (len(row) - 1):
                return True
        return False

    if position == "aisle":
        for i in free_row_indexes:
            if i == 2 or i == 4:
                return True
        return False


def get_passangers_seats(current_seats_map, row_nb, free_seats):
    row = current_seats_map[row_nb]

    for i in free_seats:
        row[int(i)] == "X"
    return None


def check_free_space_for_group(current_seats_map, num, side, position):
    count = -1
    for row in current_seats_map:
        free_space = 0
        free_row_indexes = []
        count += 1
        pass_aisle = False
        for letter in range(len(row)):
            # print(f'row: {count} - letter: {row[letter]} - free space: {free_space}')

            if row[letter] == "#":
                continue

            if row[letter] == "X":
                continue

            if row[letter] == "_":
                free_space = 0
                pass_aisle = True
                continue

            free_space += 1
            free_row_indexes.append(letter)

            # if not free_space == int(num):
            #     continue

        print(
            f"side: {side} - position: {position} - pass_aisle: {pass_aisle} - free_indexes: {free_row_indexes}"
        )
        group_req = check_group_requirements(
            row, side, position, pass_aisle, free_row_indexes
        )
        print(group_req)

        get_passangers_seats(current_seats_map, count, free_row_indexes)
        print(current_seats_map)


seats_map = []
group_map = []


row_quantity = int(input())
for i in range(row_quantity):
    seats_map.append(input())

group_quantity = int(input())
for i in range(group_quantity):
    group_map.append(input())

print()
print()

for group in group_map:
    num, side, position = decode_group_map(group)
    check_free_space_for_group(seats_map, num, side, position)
