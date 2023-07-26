#!/usr/bin/env python3
##
# write a program that reads integers from the user(0 to quit),stores them in a list and display them
# in ascending order.
#
data = []
num = int(input("Enter the number(0 to quit): "))
while num != 0:
    data.append(num)
    num = int(input("Enter the number(0 to quit): "))

# use sort(method) because we don't need save an original order
data.sort()

# display the result
for num in data:
    print(num)
