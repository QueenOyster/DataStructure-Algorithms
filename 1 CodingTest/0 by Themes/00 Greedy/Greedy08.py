import sys
import time
from collections import deque
sys.stdin = open("input.txt", 'rt')
start_time = time.time()

n = int(input())
nums = map(int, input().split())
nums = deque(nums)

result = ""
criteria = 0
while True:
    if criteria < nums[0]:
        if criteria < nums[-1] < nums[0]:
            criteria = nums[-1]
            result += "R"
            nums.pop()
        else:
            criteria = nums[0]
            result += "L"
            nums.popleft()
    elif criteria < nums[-1]:
        criteria = nums[-1]
        result += "R"
        nums.pop()
    else:
        break

print() #
print(len(result))
print(result)

end_time = time.time()
print("time: ", end_time - start_time)
print() #