import sys
sys.stdin = open('input.txt' , 'rt')
n = int(input())
grades = list(map(int, input().split()))

sum = 0
cnt = 0
for grade in grades:
    if grade == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)