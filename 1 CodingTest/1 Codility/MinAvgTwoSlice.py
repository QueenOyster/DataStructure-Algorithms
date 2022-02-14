# 80%
# Detected time complexity:O(N) or O(N ** 2)
large_num = int(1e9)

def solution(A):
    
    starting_position_memory = None
    min_average = large_num
    for i in range(len(A)-1):
        start = i
        end = i + 1
        
        while True:
            part_sum = A[start:end+1]
            current_average = sum(part_sum)/len(part_sum)
            if end+1 <= len(A)-1 and A[end+1] <= current_average:
                end += 1
            else:
                break
        
        if current_average < min_average:
            min_average = current_average
            starting_position_memory = i
    
    return starting_position_memory

# 100%
# Detected time complexity:O(N)
# "https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=alwlren_00&logNo=221603639510"

large_num = int(1e9)

def solution(A):
    
    starting_position_memory = None

    min_average = large_num
    for i in range(len(A)-1):
        part_sum = A[i:i+2]
        current_average = sum(part_sum)/2
        
        if current_average < min_average:
            min_average = current_average
            starting_position_memory = i

    for i in range(len(A)-2):
        part_sum = A[i:i+3]
        current_average = sum(part_sum)/3
        
        if current_average < min_average:
            min_average = current_average
            starting_position_memory = i
    
    return starting_position_memory