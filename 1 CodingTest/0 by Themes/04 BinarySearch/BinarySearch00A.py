# 자판기 불빛 같은 느낌
import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
db = [0] * 1000001

now_on_sale = list(map(int, input().split()))
for item in now_on_sale:
    db[item] = 1

m = int(input())
order = list(map(int, input().split()))

for item in order:
    if db[item] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')