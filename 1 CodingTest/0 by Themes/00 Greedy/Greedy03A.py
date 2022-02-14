import sys
sys.stdin = open('input.txt', 'rt')

n, k = map(int, input().split())
result = 0

# 풀이 구조 더 상세하게 분석 해서 케이스 분리
# 만약 2 <= n <= 100,000
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)