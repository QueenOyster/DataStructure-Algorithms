import sys
sys.stdin = open('input.txt', 'rt')
def TotalLength(array, current_H):
    sum = 0
    for ttuck in array:
        if ttuck <= current_H:
            continue
        else:
            sum += (ttuck - current_H)
    return sum

def BinarySearch(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        # print(mid, end= ' ') => 모니터링
        if TotalLength(array, mid) < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

n, m = map(int, input().split())
ttucks = list(map(int, input().split()))
print(BinarySearch(ttucks, 0, max(ttucks)))