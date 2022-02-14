import sys
sys.stdin = open('Floyd-Warshall-02.txt', 'rt')
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().rstrip().split())
    graph[start][end] = cost
for i in range(1, n+1):
    graph[i][i] = 0

for stopover in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end], graph[start][stopover]+graph[stopover][end])

# Debug / Answer
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("M", end=' ')
        else:   
            print(graph[i][j], end=' ')
    print()