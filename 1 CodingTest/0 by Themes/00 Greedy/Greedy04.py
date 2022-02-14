# 완료
import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
result = 0
meetings = list()
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))
meetings.sort(key = lambda x: (-x[0], -x[1]))
# 배열 시간복잡도 : O(N * logN)

start, end = meetings[0][0], meetings[0][1]
cnt = 1
for i in range(1, n):
    if meetings[i][1] <= start:
        start, end = meetings[i][0], meetings[i][1]
        cnt += 1
print(cnt)