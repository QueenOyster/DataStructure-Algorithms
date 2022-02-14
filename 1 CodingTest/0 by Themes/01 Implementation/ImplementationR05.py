import sys
sys.stdin = open('input.txt', 'rt')
n, m = map(int, input().split())

spots_sum = list()
for i in range(1, n+1):
    for j in range(1, m+1):
        spots_sum.append(i+j) # 만들기

max = -1
result = list()
for k in range(2, i+j+1):
    cnt = 0
    for spot in spots_sum:
        if spot == k:
            cnt += 1 # 세기

    if cnt > max:
        max = cnt
        result.clear()
        result.append(k) # 비교하기
    elif cnt == max:
        result.append(k)

for item in result:
    print(item, end=' ')