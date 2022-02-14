# Codility Leeseon 4, MaxCounters
# Detected time complexity: O(N + M)

import copy

def solution(N, A):
    lazy_counter = [0] * (N+1)

    current_max = 0
    new_standard = 0
    for idx in A:
        if idx <= N:
            if lazy_counter[idx] <= new_standard:
                lazy_counter[idx] = new_standard
            lazy_counter[idx] += 1 # CAUTION: list index out of range
            current_max = max(current_max, lazy_counter[idx])
        else:
            new_standard = copy.deepcopy(current_max)

    for i in range(1, N+1):
        if lazy_counter[i] <= new_standard:
            lazy_counter[i] = new_standard

    return lazy_counter[1:]