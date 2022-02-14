# DFS
import sys
sys.stdin = open('input.txt', 'rt')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
            DFS(nx, ny)
        
if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                DFS(i, j)
                cnt += 1
    print(cnt)