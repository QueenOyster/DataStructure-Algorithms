# 그리디는 정렬과 함께 풀린다
import sys
sys.stdin = open('input.txt', 'rt')

# 먼저 시작한다해서 늦게 끝나면 아무런 메리트가 없으므로,
# "빨리" 끝나는게 중요

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort(key = lambda x : (x[1], x[0]))
# 이와같은 정렬 방식이 회의를 더 꽉꽉 채워서 할 수 있을 것.

end_time = 0
cnt = 0
# 새로운 표현방법
for s, e in meeting:
    if s >= end_time:
        end_time = e
        cnt += 1
print(cnt)
