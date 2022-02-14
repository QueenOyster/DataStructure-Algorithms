import sys
sys.stdin = open('input.txt' , 'rt')
n = int(input())
figures = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10 # 어쨋든 10으로 나눈다는 아이디어가 중요
    return sum

maxx = -2147000000
for figure in figures:
    total = digit_sum(figure)
    if total > maxx:
        maxx == total
        res = figure
print(res)