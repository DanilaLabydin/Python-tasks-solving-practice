def find_country(
    N,
    min_income,
    higher_education,
    direct_children,
    Q,
    income,
    has_higher_education,
    parents_citizenship,
):
    chosen_countries = (
        min(
            {
                i + 1
                for i in range(N)
                if (direct_children[i] == 1 and parents_citizenship[j] == i + 1)
                or (
                    income[j] >= min_income[i]
                    and has_higher_education[j] >= higher_education[i]
                )
            },
            default=0,
        )
        for j in range(Q)
    )

    return chosen_countries


# Read input
N = int(input())
min_income = list(map(int, input().split()))
higher_education = list(map(int, input().split()))
direct_children = list(map(int, input().split()))
Q = int(input())
income = list(map(int, input().split()))
has_higher_education = list(map(int, input().split()))
parents_citizenship = list(map(int, input().split()))

# Call the function to get the results
result = find_country(
    N,
    min_income,
    higher_education,
    direct_children,
    Q,
    income,
    has_higher_education,
    parents_citizenship,
)

# Print the results
print(" ".join(map(str, result)))
