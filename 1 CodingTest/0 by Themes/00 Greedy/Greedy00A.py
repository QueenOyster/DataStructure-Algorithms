import sys
sys.stdin = open('input.txt', 'rt')

money_change = 1260
count = 0

# Variable Names ↑
coin_types  = [500, 100, 50, 10]

# code readability ↑ (code length ↓)
for coin in coin_types:
    count += money_change // coin
    money_change %= coin

print(count)