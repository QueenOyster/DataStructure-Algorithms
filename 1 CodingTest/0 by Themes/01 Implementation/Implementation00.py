import sys
import time
sys.stdin = open("input.txt", 'rt')
start_time = time.time()

n = int(input())
navi = list(map(str, input().split()))
# (row, column)
row = 1
column = 1
for item in navi:
    if item == 'R' and column+1 <= n:
        column += 1
    elif item == 'L' and 1<= column-1:
        column -= 1
    elif item == 'U' and 1<= row-1:
        row -= 1
    elif item == 'D' and row+1 <= n:
        row += 1
    else:
        continue

print(row, column)
end_time = time.time()
print("time: ", end_time - start_time)