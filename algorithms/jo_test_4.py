def subsets(S):
    sets = []
    len_S = len(S)
    for i in range( 1 << len_S ):
        subset = [ S[ bit ] for bit in range( len_S ) if i & ( 1 << bit ) ]
        sets.append( subset )
    return sets
    

s1 = input().split()
nominal = list(map(int, input().split()))

money_goal = s1[0]
# print()
# print(money_goal)
# print()
# money_quantity = s1[1]


# print(money_quantity)
all_money = nominal * 2
all_money.sort()
# print(all_money)


for m in subsets(all_money):
    # print(type(m), type(sum(m)), type(money_goal))
    # print(f'm: {m} - sum: {sum(m)} - goal: {money_goal} ')
    # # sm = sum(m)
    # # print(sm == money_goal)
    if int(sum(m)) == int(money_goal):
        print(len(m))
        print(*m)
        break
else:
    print(-1)