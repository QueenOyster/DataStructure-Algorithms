# BFS
from collections import deque
import sys
sys.stdin = open('input.txt', 'rt')
n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

graph = list()
for i in range(n):
    graph.append(list(map(int, input())))

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            queue = deque()
            queue.append((i, j))
            while queue:
                tmp = queue.popleft()
                graph[tmp[0]][tmp[1]] = 1  # 변수 남용 금지
                for k in range(4):
                    nx = tmp[0] + dx[k]
                    ny = tmp[1] + dy[k]
                    if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                        queue.append((nx, ny))
            cnt += 1
print(cnt)