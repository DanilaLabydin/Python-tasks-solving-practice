def find_set(x, parent):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x], parent)  # Path compression
    return parent[x]

def unite_sets(x, y, parent, size):
    x = find_set(x, parent)
    y = find_set(y, parent)
    
    if x != y:
        if size[x] < size[y]:
            x, y = y, x  # Union by size
        parent[y] = x
        size[x] += size[y]

def main():
    n, m = map(int, input().split())
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    answers = []

    for _ in range(m):
        query = input().split()
        if query[0] == '1':
            x, y = map(int, query[1:])
            unite_sets(x, y, parent, size)
        elif query[0] == '2':
            x, y = map(int, query[1:])
            if find_set(x, parent) == find_set(y, parent):
                answers.append("YES")
            else:
                answers.append("NO")
        elif query[0] == '3':
            x = int(query[1])
            gang_size = size[find_set(x, parent)]
            answers.append(str(gang_size))

    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()