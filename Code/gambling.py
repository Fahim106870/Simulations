import random

total_cost = 0
total_income = 0

print("{:<10} {:<5} {:<14} {:<8} {:<6} {:<6} {:<10}".format(
    "Game No", "Sl", "Random Number", "Result", "Heads", "Tails", "Difference"))

for game in range(1, 11):  # 10 games
    h = 0
    t = 0
    sl = 0
    while True:
        sl += 1
        total_cost += 1
        r = random.randint(0, 9)
        result = "Head" if r == 0 else "Tail"
        if r <= 4:
            h += 1
        else:
            t += 1
        diff = abs(h - t)
        print("{:<10} {:<5} {:<14} {:<8} {:<6} {:<6} {:<10}".format(
            game, sl, r, result, h, t, diff))
        if diff >= 3:
            total_income += 8
            print("=> Game {} won $8 after {} tosses (Cost: ${})\n".format(game, sl, sl))
            break

print("Total Cost: ${}".format(total_cost))
print("Total Income: ${}".format(total_income))
