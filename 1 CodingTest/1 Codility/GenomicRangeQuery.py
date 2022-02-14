# Codility Lesson 5
# GenomicRangeQuery

# 1st, 영어문장 이해 못함

# 2nd, performance 나빠도 correctness 높으면 점수 받음
# O(N * M)

def solution(S, P, Q): 
    
    result = []
    for i in range(len(P)):
        deduplicated_seq = set(S[P[i]:Q[i]+1])
        
        if "A" in deduplicated_seq:
            min_factor = 1
        elif "C" in deduplicated_seq:
            min_factor = 2
        elif "G" in deduplicated_seq:
            min_factor = 3
        else:
            min_factor = 4

        result.append(min_factor)
    return result

# 3rd
# O(N * M)

def solution(S, P, Q):

    min_factors = list()
    S = list(S) # 무조건 모든 sequence의 정보를 알아놓을 필요가 있을까?
    for char in S:
        if char == "A":
            min_factors.append(1)
        elif char == "C":
            min_factors.append(2)
        elif char == "G":
            min_factors.append(3)
        else:
            min_factors.append(4)

    result = []
    for i in range(len(P)):
        result.append(min(min_factors[P[i]:Q[i]+1]))

    return result

# 4th
# O(N * M)

large_number = int(1e9)

def solution(S, P, Q):

    result = list()
    S = list(S) # CAGCCTA
    for i in range(len(P)): # 3
        start_index = P[i]
        end_index = Q[i]
        min_factor = large_number
        for idx in range(start_index, end_index+1):
            if type(S[idx]) == int:
                pass
            else:
                if S[idx] == "A":
                    S[idx] = 1
                elif S[idx] == "C":
                    S[idx] = 2
                elif S[idx] == "G":
                    S[idx] = 3
                else:
                    S[idx] = 4
            min_factor = min(min_factor, S[idx])
            if min_factor == 1:
                break
        result.append(min_factor)

    return result

https://nachwon.github.io/GenomicRangeQuery/

# 87% version
# O(N + M)

import copy

def solution(S, P, Q):

    all_counted = [[0, 0, 0, 0]]
    current_count = [0, 0, 0, 0]
    for char in S:
        if char == "A":
            current_count[0] += 1
        elif char == "C":
            current_count[1] += 1
        elif char == "G":
            current_count[2] += 1
        elif char == "T":
            current_count[3] += 1
        tmp = copy.deepcopy(current_count)
        all_counted.append(tmp)

    result = []
    for i in range(len(P)):
        for j in range(4):
            tmp = all_counted[Q[i]+1][j] - all_counted[P[i]][j]
            if tmp >= 1:
                result.append(j+1)
                break

    return result

# 100% version
# O(N + M)? O(N * M)?

def solution(S, P, Q):
    
    M = len(P)
    
    return_arr = []
    
    for i in range(M):
        arr = S[P[i]:Q[i]+1]
        try:
            arr.index('A')
            return_arr.append(1)
        except:
            try:
                arr.index('C')
                return_arr.append(2)
            except:
                try:
                    arr.index('G')
                    return_arr.append(3)
                except:
                    return_arr.append(4)
                    
    return return_arr

# 'in' ver

def solution(S, P, Q):
    
    return_arr = []
    
    M = len(P)
    for i in range(M):
        arr = S[P[i]:Q[i]+1]
        if 'A' in arr:
            return_arr.append(1)
        elif 'C' in arr:
            return_arr.append(2)
        elif 'G' in arr:
            return_arr.append(3)
        else:
            return_arr.append(4)
                    
    return return_arr