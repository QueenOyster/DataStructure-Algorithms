# 이것이 코딩 테스트다, p.262 - 전보

import heapq
import sys
sys.stdin = open("Dijkstra-01.txt", 'rt')
n, m, city = map(int, sys.stdin.readline().rstrip().split())

INF = int(1e9)
time_cost = [INF] * (n+1)

graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    time_cost[start] = 0
    while q:
        each_time, now = heapq.heappop(q)
        if time_cost[now] < each_time:
            continue
        
        for i in graph[now]:
            cost = each_time + i[1]
            if cost < time_cost[i[0]]:
                time_cost[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))    

dijkstra(city)

# Debug
cnt = 0
max_time = 0
for each_time in time_cost:
    if 0 < each_time < INF:
        cnt += 1
        max_time = max(max_time, each_time)
print(cnt, max_time)