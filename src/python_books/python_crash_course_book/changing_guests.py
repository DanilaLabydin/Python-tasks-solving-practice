#!/usr/bin/env python3
##
# write a program that prints list of my friends, then delete a person that can't make the dinner
# and replace the name of the guest who can't make it with the name of the new person
#
print("I invite some friends to the dinner: ")
invited_friends = ["Polya", "Tema", "Sanya", "Vova", "Arch"]
for friend in invited_friends:
    print(f"{friend}, I invite you to the diner!")
print(f"But {invited_friends[3]} can't make it")
deleted_friend = invited_friends.pop(3)
invited_friends.insert(3, "Taras")
for friend in invited_friends:
    print(f"{friend}, I invite you to the diner!")
print("I found a bigger dinner table")
invited_friends.insert(0, "Kir")
invited_friends.append("Max")
invited_friends.insert(len(invited_friends) // 2, "Misha")
for friend in invited_friends:
    print(f"{friend}, I invite you to the diner!")
print("Unfortunately, i have space for only two guests :(")
print(len(invited_friends))
for i in range(len(invited_friends) - 2):
    deleted_friend = invited_friends.pop()
    print(f"{deleted_friend}, sorry, I don't have enough place tonight")
for friend in invited_friends:
    print(f"{friend} you still on my list")
del invited_friends[0]
del invited_friends[0]
print(invited_friends)
