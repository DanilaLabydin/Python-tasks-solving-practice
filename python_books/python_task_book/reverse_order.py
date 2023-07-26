#!/usr/bin/env python3
##
# write a program that reads integers from the user and stores them in a list, then displays
# the list in reverse order
#
data = []
num = int(input("Enter the number(0 to quit): "))
while num != 0:
    data.append(num)
    num = int(input("Enter the number(0 to quit): "))

# sort the list in reverse order
data.reverse()

# display the result
for num in data:
    print(num)
