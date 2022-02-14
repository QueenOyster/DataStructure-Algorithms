# 팀 결성
# 이것이 코딩테스트다, p.298

import sys
sys.stdin = open('Union-Find-01.txt', 'rt')
n, m = map(int, input().split())
parent = [0] * (n+1)
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) # Path Compression
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    bit, a, b = map(int, sys.stdin.readline().rstrip().split())

    if bit == 0:
        union_parent(parent, a, b)
    elif bit == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")