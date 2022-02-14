# Codility Lesson 5, CountDiv

# 1st
# '0'을 고려하지 않아서 틀림
# Detected time complexity: for loop O, O(B-A)~O(N)
def solution1(A, B, K):
    if B < K:
        return 0 
    ...

# 2nd
# Detected time complexity: O(1)

def solution2(A, B, K):
    A1 = A // K
    A2 = A % K
    B1 = B // K
    B2 = B % K

    if A1 < B1:
        if A2 == 0:
            return B1 - (A1 - 1)
        else:
            return B1 - A1
    else: # A1 == B1
        if A2 == 0:
            return 1
        else:
            return 0