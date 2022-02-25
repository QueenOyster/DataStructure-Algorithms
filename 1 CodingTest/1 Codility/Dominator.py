# Lesson 8: Leader
# O(N*log(N)) or O(N)

def solution(A):
    
    counter = dict()
    N = len(A)
    for i in range(N):
        if A[i] in counter.keys():
            counter[A[i]] += 1
        else:
            counter[A[i]] = 1
        if counter[A[i]] > N/2:
            return i
    else:
        return -1