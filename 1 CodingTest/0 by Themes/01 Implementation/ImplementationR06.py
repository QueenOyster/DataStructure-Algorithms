import sys
sys.stdin = open('input.txt', 'rt')

def digit_sum(x):
    sum = 0
    while x:
        rem = x % 10
        sum += rem
        x = (x-rem)/10
    return sum

n = int(input())
figures = list(map(int, input().split()))

maxx = -1
for fig in figures:
    current_sum = digit_sum(fig)
    if current_sum > maxx:
        maxx = current_sum
        fig_memory = fig
print(fig_memory)