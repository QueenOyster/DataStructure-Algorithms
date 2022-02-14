import sys
sys.stdin = open('Floyd-Warshall-01A.txt', 'rt')
n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

# Initialize
for i in range(1, n+1):
    graph[i][i] = 0
for _ in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    graph[start][end] = 1
    graph[end][start] = 1

x, k = map(int, input().split()) # 잘 읽는 능력 중요

# Floyd-Warshall
for stopover in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end], graph[start][stopover] + graph[stopover][end])

distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)

# Debug
# for row in graph:S
#     for element in row:
#         if element == INF:
#             print("%4s" % "INF", end=' ')
#         else:
#             print("%4d" % element, end=' ')
#     print()