import sys
sys.stdin = open('input.txt', 'rt')
n, m = map(int, input().split())

count = [0] * (n + m + 1)
for i in range(1, n+1):
    for j in range(1, m+1):
        count[i+j] += 1 # 세기만 하면 됨, 만들기는 필요없음

maxx = -2147000000 # 비교하기, 결과값 찾기
result = list()
for idx, num in enumerate(count):
    if num > maxx:
        maxx = num
        result.clear()
        result.append(idx)
    elif num == maxx:
        result.append(idx)

for item in result: # 보여주기
    print(item, end=' ')