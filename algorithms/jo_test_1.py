num1 = input().split()
num2 = input().split()


guns_nb = int(num1[0])
money = int(num1[1])

# print(guns_nb)
# print(money)

best = 0
for gun in num2:
    gun_price = int(gun)
    if gun_price > money:
        continue
    
    best = max(best, gun_price)

print(best)
