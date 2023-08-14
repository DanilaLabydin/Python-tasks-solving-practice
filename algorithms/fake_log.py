import datetime


nb = int(input())
time_log = [(input()) for i in range(nb)]

days_nb = 1
first_log_record = time_log[0]
for i in range(1, len(time_log)):
    curr_log = time_log[i]
    curr_time = datetime.datetime.strptime(curr_log, "%H:%M:%S")

    prev_log = time_log[i - 1]
    prev_time = datetime.datetime.strptime(prev_log, "%H:%M:%S")

    if curr_time <= prev_time:
        days_nb += 1

print(days_nb)


# print(time_log[i])
# print(type(time_log[i]))
# print(i)
# time = datetime.datetime(str(time_log[i]), '%H:%M:%S')
# print(time)
# hour, minute, second = time_log[i]

# if int(hour) < int(time_log[i-1][0]):
#     days_nb += 1
#     continue

# else:
#     if int(minute) < int(time_log[i-1][1]):
#         days_nb += 1
#         continue

#     else:
#         if int(second) <= int(time_log[i-1][2]):


# if int(hour) <= int(time_log[i-1][0]) and int(minute) <= int(time_log[i-1][1]) and int(second) <= int(time_log[i-1][2]):
#     days_nb += 1
# print(time_log[i])
