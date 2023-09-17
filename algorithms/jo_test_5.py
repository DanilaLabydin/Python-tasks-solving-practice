def find_states(n, m, roads):
    def find(parent, city):
        if parent[city] != city:
            parent[city] = find(parent, parent[city])
        return parent[city]

    def union(parent, city1, city2):
        root1 = find(parent, city1)
        root2 = find(parent, city2)
        if root1 != root2:
            parent[root2] = root1

    def count_states(parent):
        states = set()
        for i in range(1, n + 1):
            states.add(find(parent, i))
        return len(states)

    # Sort roads by length in ascending order
    roads.sort(key=lambda x: x[2])

    # Initialize parent array for Union-Find
    parent = [i for i in range(n + 1)]

    # Binary search to find the minimum x
    left, right = 0, int(1e9)
    result = right

    while left <= right:
        mid = (left + right) // 2
        valid = True

        # Reset parent array
        for i in range(1, n + 1):
            parent[i] = i

        for u, v, w in roads:
            if w > mid:
                union(parent, u, v)

        if count_states(parent) == 1:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

# Input
n, m = map(int, input().split())
roads = []
for _ in range(m):
    u, v, w = map(int, input().split())
    roads.append((u, v, w))

# Find and print the result
result = find_states(n, m, roads)
print(result)