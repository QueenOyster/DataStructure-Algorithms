import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
athletes = list()
for _ in range(n):
    height, weight = map(int, input().split())
    athletes.append((height, weight))
athletes.sort(key= lambda x : -x[1])

# largest를 찾고 비교한다는 의미?
# 이전 값들중 가장 큰놈(largest)보다 작으면 어짜피 뽑히지 못한다.
# time complexity: O(n^2) -> O(n)
cnt = 0
largest = 0
for i in range(n):
    if athletes[i][0] > largest:
        largest = athletes[i][0]
        cnt += 1
print(cnt)