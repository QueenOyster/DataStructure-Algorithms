import sys
import time
from collections import deque # 왜? list가 맨 앞의 값 꺼낼때 한칸씩 당겨지는 비효율 있기 때문
sys.stdin = open("input.txt", 'rt')
start_time = time.time()

nums, limit = map(int, input().split())
people = list(map(int, input().split()))
people.sort() # deque 자료형으로는 sort 불가능
people = deque(people)
cnt = 0

while people:
    if len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.popleft()
    people.pop()
    cnt += 1
print(cnt)

end_time = time.time()
print("time: ", end_time - start_time)