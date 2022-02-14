# Iterative Pattern(Parametric Search)
import sys
sys.stdin = open('input.txt', 'rt')
n, m = list(map(int, input().split()))
ttucks = list(map(int, input().split()))

start = 0
end = max(ttucks)
while(start <= end):
    total_length = 0
    mid = (start + end) // 2
    # print(mid)
    
    for ttuck in ttucks:
        if ttuck > mid:
            total_length += (ttuck - mid)
    
    if total_length < m:
        end = mid - 1 # 더 길게 자르기 위해
    else:
        result = mid
        start = mid + 1 # 더 짧게 자르기 위해
print(result)