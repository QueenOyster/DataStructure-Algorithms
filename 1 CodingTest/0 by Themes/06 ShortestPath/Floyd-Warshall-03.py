# Inflearn - 회장뽑기

import sys
sys.stdin = open('Floyd-Warshall-03.txt', 'rt')
n = int(input())
INF = int(1e9)

# Graph
graph = [[INF] * (n+1) for _ in range(n+1)]
while True:
    start, end = map(int, sys.stdin.readline().rstrip().split())
    if start == -1 and end == -1:
        break
    graph[start][end] = 1
    graph[end][start] = 1
for i in range(1, n+1):
    graph[i][i] = 0

# Find Shortest Path 
for stopover in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end], graph[start][stopover]+graph[stopover][end])

# Debug
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if graph[i][j] == INF:
#             print("M", end=' ')
#         else:   
#             print(graph[i][j], end=' ')
#     print()

# Find Answer
score = INF
result = list()
for i in range(1, n+1):
    if max(graph[i][1:]) < score:
        result.clear()
        result.append(i)
        score = max(graph[i][1:])
    elif max(graph[i][1:]) == score:
        result.append(i)

# Output
print(score, len(result))
for item in result:
    print(item, end=' ')