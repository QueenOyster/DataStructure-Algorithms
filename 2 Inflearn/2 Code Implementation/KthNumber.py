# K번째 수

#########################################
######## My Code, O(T * Nlog(N)) ########
#########################################

import sys
# sys.stdin = open('in1.txt', 'rt')

T = int(input())
for i in range(T):
    n, s, e, k = map(int, input().split())
    tmpList = list(map(int, input().split()))[s-1:e]
    # print(tmpList)
    tmpList.sort()
    print('#', end='')
    print(i+1, tmpList[k-1])


#########################################
##### Answer Code, O(T * Nlog(N)) #######
#########################################

import sys
# sys.stdin=open("input.txt", "r")

T=int(input())
for t in range(T):
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split()))
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1])) # Format