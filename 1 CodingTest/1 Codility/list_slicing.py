# TapeEquilibrium
# Codility, Lesson3 

large_num = int(1e9)
def solution(A):
    # Error Input
    if len(A) < 2:
        return 0
    
    mindiff = large_num
    sum_left = 0
    sum_total = sum(A)
    for i in range(0, len(A)-1): # len(A)- 1: Hand-Writing
        sum_left += A[i]
        # SL + SR = S, SL - SR = SL - (S - SL) = 2SL - S
        diff = abs(2 * (sum_left) - (sum_total))
        mindiff = min(mindiff, diff)
    return mindiff

# Time Over - list slicing: O(N^2)
# challenger = abs(sum(A[:i]) - sum(A[i:])) # CAUTION! out of range index