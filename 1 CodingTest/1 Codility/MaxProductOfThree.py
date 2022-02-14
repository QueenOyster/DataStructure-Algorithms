# Codility Lesson 6, MaxProductOfThree
# 100%, O(N * log(N))

smallest_number = -int(1e10)

def solution(A):
    A.sort()
    
    maximum = max(smallest_number, A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])

    return maximum