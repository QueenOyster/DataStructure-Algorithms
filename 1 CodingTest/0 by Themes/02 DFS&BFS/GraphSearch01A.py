# DFS
import sys
sys.stdin = open('input.txt', 'rt')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, L):
    global result
    footprints[x][y] = 0
    if x == n-1 and y == m-1:
        result = min(result, L)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and footprints[nx][ny] == 1:
                DFS(nx, ny, L+1)
                footprints[nx][ny] = 1

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = list()
    footprints = graph
    for _ in range(n):
        graph.append(list(map(int, input())))
    result = 2147000000
    DFS(0, 0, 1)
    print(result)