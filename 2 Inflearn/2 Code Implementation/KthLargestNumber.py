# K번째 큰 수

#####################################################
########### My Code, O(N^3), max(N) = 100 ###########
#####################################################

import sys
# import os
# currentPath = os.getcwd()
# os.chdir(currentPath+"\\3. k번째 큰 수") # 1. FileNotFoundError
# sys.stdin = open('in2.txt', 'rt')

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = 0
tmpList = list()
for x in range(n):
    for y in range(x+1, n):
        for z in range(y+1, n): ## 2. Repeated Variable
            tmpList.append(numbers[x] + numbers[y] + numbers[z])
            # print(numbers[x], numbers[y], numbers[z])
tmpList = set(tmpList) # 3. O(length of iterable)
tmpList = list(tmpList)
tmpList.sort(reverse=True)

print(tmpList[k-1])

# 4. Greedy 식의 접근은 틀렸음(반례 존재)
# for x in range(n):
#     for y in range(x+1, n):
#         for z in range(y+1, n): ## 2. Repeated Variable
#             cnt += 1
#             if cnt == k:
#                 print(numbers[x], numbers[y], numbers[z])
#                 print(x, y, z)
#                 print(numbers[x] + numbers[y] + numbers[z])

# 5. 문제를 제대로 읽어라.. 문제만 10분봐도 됨


###################################################
########## Answer Code, O(N^3) ####################
###################################################


import sys
sys.stdin=open("input.txt", "r")
n, k=map(int, input().split())
a=list(map(int, input().split()))
res=set() # 처음부터 집합으로 받기
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res=list(res)
res.sort(reverse=True)
print(res[k-1])