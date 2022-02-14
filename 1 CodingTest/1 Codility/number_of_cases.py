# Detected time complexity:O(N) or O(N * log(N))
# Codility Lesson 4, MissingInteger

def solution(A):
    
    A = set(A)
    A = list(A)
    A.sort()

    # そもそもAに1以上の元素がない時
    if A[-1] <= 0:
        return 1
    
    # Aに1以上の元素があって、陽数たちに非連続的である時
    expected_num = 1
    for element in A:
        if element >= 1:
            if element != expected_num:
                return expected_num
            expected_num += 1
    # Aに1以上の元素があって、陽数たちに非連続的がない時
    return A[-1] + 1