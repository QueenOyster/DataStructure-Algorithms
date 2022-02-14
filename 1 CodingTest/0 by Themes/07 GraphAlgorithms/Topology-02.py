# Inflearn, 위상정렬(그래프 정렬)

import sys
from collections import deque
sys.stdin = open('Topology-02.txt', 'rt')
n, m = map(int, input().split())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque() 
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for end_node in graph[now]:
            indegree[end_node] -= 1
            if indegree[end_node] == 0:
                q.append(end_node)
    for node in result:
        print(node, end=' ')

topology_sort() # 1 6 2 5 4 3