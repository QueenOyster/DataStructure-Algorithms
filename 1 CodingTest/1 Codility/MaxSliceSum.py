# Lesson 9
# O(N)

def solution(A):
  
    max_ending = max_slice = 0

    largest_non_positive = -2147483648
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
        if a <= 0:
            largest_non_positive = max(largest_non_positive, a)

    
    if max_slice > 0:
        return max_slice
    elif max_slice == 0:
        return largest_non_positive