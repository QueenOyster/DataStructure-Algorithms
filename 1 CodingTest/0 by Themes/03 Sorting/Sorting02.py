import sys
sys.stdin = open('input.txt', 'rt')
n, k =map(int, input().split())

array_A = list(map(int, input().split()))
array_A.sort()
array_B = list(map(int, input().split()))
array_B.sort(reverse=True)

for i in range(k):
    if array_A[i] < array_B[i]: 
        array_A[i], array_B[i] = array_B[i], array_A[i]
print(sum(array_A))