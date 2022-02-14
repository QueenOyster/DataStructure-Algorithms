import sys
sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
# 1 <= number <= 10000 이므로
res = 0
for _ in range(n):
    data = list(map(int, input().split()))
    data.sort()
    res = max(res, data[0])
print(res)