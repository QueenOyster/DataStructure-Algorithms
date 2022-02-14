import sys
sys.stdin = open('input.txt', 'rt')

n, k = map(int, input().split())
result = 0

# 만약 n >= 1,000,000,000
while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    n //= k
    result += 1

result += (n - 1)
print(result)