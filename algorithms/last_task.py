def calculate_spell_strength(N, K, S, p, d):
    total_strength = 0  # Variable to store the total strength of all spells

    for start_pos in range(N):
        unique_chars = set()  # Set to store unique characters encountered in each spell

        current_pos = start_pos
        spell_length = 0

        while spell_length < K:
            char = S[current_pos]
            unique_chars.add(char)

            current_pos = p[current_pos] - 1  # Convert to 0-based index
            current_pos = (current_pos + d[current_pos]) % N

            spell_length += 1

        total_strength += len(unique_chars)

    return total_strength


# Read input
N, K = map(int, input().split())
S = input()
p = list(map(int, input().split()))
d = list(map(int, input().split()))

# Calculate and print the total strength of all spells
result = calculate_spell_strength(N, K, S, p, d)
print(result)
