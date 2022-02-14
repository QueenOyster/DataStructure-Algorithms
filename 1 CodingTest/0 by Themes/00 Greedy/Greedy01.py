import sys
sys.stdin = open('input.txt', 'r')

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

sum = 0
for idx in range(m):
    if (idx+1)%(k+1) != 0:
        sum += numbers[0]
    else:
        sum += numbers[1]
print(sum)