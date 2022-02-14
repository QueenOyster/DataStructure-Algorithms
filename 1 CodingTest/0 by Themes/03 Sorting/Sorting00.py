import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())

array = list()
for _ in range(n):
    array.append(int(input()))
array.sort(reverse=True)

for num in array:
    print(num, end=' ')