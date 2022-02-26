시간 복잡도: O(N) --> 100%의 정답률

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    right_map = {}
    left_map = {}
    
    for i in A:
        try:
            right_map[i] += 1
        except:
            right_map[i] = 1
    
    count = 0
    left_leader = 0
    left_length = 0
    right_length = len(A)
    left_leader_count = 0
   
    for i in range(len(A)):
        right_map[A[i]] -= 1
        right_length -= 1
        
        try:
            left_map[A[i]] += 1
        except:
            left_map[A[i]] = 1
            
        left_length += 1
        
        # get left leader
        if left_map[A[i]] > left_leader_count:
            left_leader = A[i]
            left_leader_count = left_map[A[i]]
        
        # get equi leader
        if right_map[left_leader] > right_length//2 and left_leader_count > left_length//2: 
            count += 1
        
    
    return count