import sys
sys.stdin = open('input.txt' , 'rt')
n = int(input())
figures = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    for digit in str(x):
        sum += int(digit) # 장점: 파이썬만의 처리방식
    return sum

maxx = -2147000000 # C++ 기준
for figure in figures:
    total = digit_sum(figure)
    if total > maxx:
        maxx == total
        res = figure
print(res)