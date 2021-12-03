test1 = '?ab??a'
test2 = 'bab??a'
test3 = '?a?'


def solution(string):
    list_char = []
    new_string = ''
    for char in string:
        list_char.append(char)

    for item in range(0, len(list_char)):
        first = list_char[item]
        last = list_char[- (item + 1)]
        print(f'{first} {last}')

        if first == '?' and last == '?':
            new_string += 'a'

        elif first == last:
            new_string += first

        elif first == '?' and last != '?':
            new_string += last

        elif first != '?' and last == '?':
            new_string += first

        elif first != last:
            return 'NO'

    return new_string



def main():
    print(solution(test3))
    print()
    print(solution(test2))
    print()
    print(solution(test1))

if __name__ == '__main__':
    main()


