# K번째 약수

###############################
######## My Code, O(N) ########
###############################

import sys
# sys.stdin = open('input.txt', 'rt')

n, k = map(int, input().split())
order = 0
for i in range(1, n+1):
    if n % i == 0:
        order += 1
        if order == k:
            print(i)
            break
else:
    print(-1)

###############################
###### Answer Code, O(N) ######
###############################

import sys
# sys.stdin=open("input.txt", "r")

n, k=map(int, input().split())
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)