import sys
sys.stdin = open('input.txt' , 'rt')
n = int(input())
grades = list(map(int, input().split()))

score = 0
combo = 0
for i in range(n):
    if grades[i] == 1:
        score += (1 + combo)
        combo += 1
    else:
        combo = 0
print(score)