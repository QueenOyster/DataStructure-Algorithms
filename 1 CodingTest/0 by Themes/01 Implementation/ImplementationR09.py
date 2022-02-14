import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())

minn = -2147000000
for _ in range(n):
    dices = list(map(int, input().split()))

    if len(set(dices)) == 3: # x, y, z
        tmp = sorted(dices)[2] * 100
    elif len(set(dices)) == 2: # x, x, y
        tmp = 1000 + sorted(dices)[1] * 100
    elif len(set(dices)) == 1: # x, x, x
        tmp = 10000 + sorted(dices)[0] * 1000

    if tmp > minn:
        minn = tmp

print(minn)