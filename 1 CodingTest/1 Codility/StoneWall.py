# Lesson 7
# O(N), 100%

def solution(H):
    
    temp_stack = list()
    block_cnt = 0
    for i in range(len(H)):

        if not temp_stack:
            block_cnt += 1
            temp_stack.append(H[i])

        else: # temp_stack:
            if temp_stack[-1] == H[i]:
                continue
            else: # temp_stack[-1] != H[i]
                if temp_stack[-1] < H[i]:
                    block_cnt += 1
                    temp_stack.append(H[i])
                else: # temp_stack[-1] > H[i]
                    while True:
                        if temp_stack:
                            temp_stack.pop() # 일단 맨위에꺼 재껴놓고
        
                            if not temp_stack:
                                block_cnt += 1
                                temp_stack.append(H[i])
                                break    

                            if temp_stack[-1] == H[i]: # 높이가 같은경우
                                break
                            elif temp_stack[-1] < H[i]:
                                block_cnt += 1
                                temp_stack.append(H[i]) 
                                break
                            else: # temp_stack[-1] > H[i]
                                continue # 높이가 작은경우, 내리다 보면 같은높이가 있을지도, 계속 내려봐야
                                    
                        elif not temp_stack: # 그런데 내리다가 모든것을 다 소진하면 그냥 없는것임
                            block_cnt += 1
                            temp_stack.append(H[i])
    return block_cnt