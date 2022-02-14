# Codility Lesson 6
# Distinct 

# 100%
# O(N*log(N)) or O(N)

def solution(A):
    
    if not A:
        return 0

    counter = [0] * 2000000

    for element in A:
        if counter[element+1000000] == 0:
            counter[element+1000000] = 1

    result = 0
    for count in counter:
        if count == 1:
            result += 1

    return result

# 100%
# O(N*log(N)) or O(N)

def solution(A):
    
    if not A:
        return 0

    A.sort()
    A = set(A)
    return len(A)

# 번외
# 100%
# O(N*log(N)) or O(N)

import collections
def solution(A):

    count_num = collections.defaultdict(int)

    for i in A:
        count_num[i] += 1

    return len(count_num.keys())