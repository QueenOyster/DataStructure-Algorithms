# BFS
from collections import deque
import sys
sys.stdin = open('input.txt', 'rt')
n, m = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

graph = list()
for _ in range(n):
    graph.append(list(map(int, input())))

queue = deque()
queue.append((0, 0))
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))
print(graph[n-1][m-1])