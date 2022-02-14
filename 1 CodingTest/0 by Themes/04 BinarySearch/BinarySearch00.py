import sys
sys.stdin = open('input.txt', 'rt')
def BinarySearch(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return BinarySearch(array, target, start, mid - 1)
    else:
        return BinarySearch(array, target, mid + 1, end)

n = int(input())
store = list(map(int, input().split()))
store.sort()

m = int(input())
order = list(map(int, input().split()))
for i in range(m):
    if BinarySearch(store, order[i], 0, len(store) - 1) != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')