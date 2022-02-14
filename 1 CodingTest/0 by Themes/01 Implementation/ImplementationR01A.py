import sys
sys.stdin = open('input.txt', 'rt')
n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k: # 따로 list 만들 필요 없이 바로 세기, 공간 최적화
        print(i)
        break # 필요한 정보만 얻고 중단, 시간 최적화
else:
    print(-1)
