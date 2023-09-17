def first_question(x, y, bands, changes):
    x_band = []
    y_band = []
    for band in bands:
        if x in band:
            x_band = band
        
        if y in band:
            y_band = band

    if x_band is y_band:
        for i in x_band:
            changes[i] += 1
        return
    
    union_band = x_band + y_band
    bands.append(union_band)
    for i in union_band:
        changes[i] += 1


def second_question(x, y, bands):
    x_band = []
    y_band = []
    for band in bands:
        if x in band:
            x_band = band
        
        if y in band:
            y_band = band

    if x_band is y_band:
        print('YES')
        return

    print('NO')
    return


def third_question(x, changes):
    print(changes.get(x))


n, m = map(int, input().split())
questions = []

for i in range(m):
    questions.append(tuple(input().split()))

bands = []
changes = {}

for i in range(1, n + 1):
    bands.append([i])
    changes[i] = 1

print(bands)
print(changes)

for question in questions:
    if question[0] == "1":
        x = int(question[1])
        y = int(question[2])

        first_question(x, y, bands, changes)
        # print(f'bands: {bands} - changes: {changes}')

    elif question[0] == "2":
        x = int(question[1])
        y = int(question[2])
        second_question(x, y, bands)

    elif question[0] == "3":
        x = int(question[1])
        # print(f'x: {x}')
        third_question(x, changes)
