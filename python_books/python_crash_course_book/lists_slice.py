#!/usr/bin/env python3


def main():
    names = ["Mama", "Papa", "Max", "Lena", "John", "Mike", "Pam", "Ray"]
    print("The first three items in the list are:", end=" ")
    print(names[:3])
    print("The two items from the middle of the list are: ", end=" ")
    print(names[(len(names) // 2) : (len(names) // 2) + 2])
    print("The last three items in the list are: ", end=" ")
    print(names[-1:-4:-1])

    dimensions = (200, 50)
    print(dimensions)
    print(dimensions[0])
    print(dimensions[1])

    # to define a tuple with one element
    my_t = (3,)

    for dimension in dimensions:
        print(dimension)

    # if you want to modify a tuple, you need to redefine it
    print("Original dimensions: ")
    for i in dimensions:
        print(i)
    print("Modify dimensions: ")
    for i in dimensions:
        print(i)


if __name__ == "__main__":
    main()
