import sys
sys.stdin = open('input.txt' ,'rt')
n = int(input())
db = set(map(int, input().split())) # 특정 자료 존재 유무 검사: set

m = int(input())
order = list(map(int, input().split()))

for item in order:
    if item in db:
        print('yes', end=' ')
    else:
        print('no', end=' ')