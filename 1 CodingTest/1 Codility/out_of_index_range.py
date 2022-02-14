# PermMissingElem
# Codility, Lesson3 

def solution(A):
    if not A: # whether list is empty or not
        return 1

    A.sort()
    # Grouping by using general input
    if A[0] == 2: 
        return 1
    for i in range(len(A)-1):
        if A[i] + 1 != A[i+1]: # CAUTION! out of index range 
            return A[i] + 1
    else:
        return A[-1] + 1  