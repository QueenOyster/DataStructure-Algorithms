# Lesson 7
# 37%

def solution(A, B):
    N = len(A)
    fight = 0
    result = 0
    for i in range(N):
        if fight == 0:
            if B[i] == 0:
                result += 1
            else: 
                fight = 1 # battle start
                result += 1 # only 1 fish will alives
                power = A[i]
        else:
            if B[i] == 0: # battle
                if power < A[i]:
                    fight = 0
                else:
                    continue
            else:
                result += 1
                power = A[i]
    return result