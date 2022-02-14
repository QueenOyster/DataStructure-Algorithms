import sys
sys.stdin = open('input.txt', 'rt')

# 세로 n, 가로 m
n, m = map(int, input().split())
# 세로 a, 가로 b, 방향 i(d'i'rection)
a, b, i = map(int, input().split())
vectors = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북동남서

# map 정보 입력
mapp = list()
for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

# 밟은 자리 수
cnt = 0
# 향후 갈 곳
plans = [(a, b)]
while plans: # 갈 곳이 있는 동안은 반복
    current = plans.pop() # 현재위치
    mapp[current[0]][current[1]] = 1 # 발도장 찍기
    cnt += 1 # 방문한 칸의 수 +1
    # print(current[0], current[1]) -> 모니터링
    for _ in range(4): # 4 방향
        i = (i - 1)%4 # 새 방향 정하기
        # 새로운 '예비' 좌표
        new_a = current[0] + vectors[i][0]
        new_b = current[1] + vectors[i][1]
        # 조건: 맵 안에 있으며 & 가지 않은 곳
        if 0<= new_a < n and 0 <= new_b < m and mapp[new_a][new_b] == 0:
            plans.append((new_a, new_b))
            break # 새로 갈 곳 찾으면 중지
    else: # 갈 곳 못찾았을 경우 -> 현재 보는(초기) 방향의 뒤로
        new_a = current[0] + vectors[(i-2)%4][0] # 새 방향 정하기
        new_b = current[1] + vectors[(i-2)%4][1]
        # 갈 수 있는 곳이라면
        if 0<= new_a < n and 0 <= new_b < m and mapp[new_a][new_b] == 0:
            plans.append((new_a, new_b)) # 그 곳으로
        else: # 거기도 못간다
            print(cnt) # cnt 출력 후 코드 종료
            sys.exit(0)
print(cnt) # 정상종료시 마지막에 cnt 출력