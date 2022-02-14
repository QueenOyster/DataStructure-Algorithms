# SourcecodeCopyrightText: CC BY-NC-SA 2020. Dongbin Na
# 이것이 코딩테스트다, p.300~301

import sys
sys.stdin = open('Kruskal-01.txt', 'rt')

# Input 1: Vertex, Edge
n, m = map(int, input().split())
# Input 2: Edges' Cost
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

# func 1
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
# func 2
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b
    

# Reset Parent
parent = [0] * (n+1) 
for i in range(1, n+1):
    parent[i] = i
# Kruskal Algorithm
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last_cost = cost

# Output
print(result - last_cost) # 8