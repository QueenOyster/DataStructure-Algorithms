import sys
sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 1 <= number <= 10000 이므로
    min_value = 10001
    for a in data:
        # list를 sort하지 않고 for문을 돌며 min값 확인
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)