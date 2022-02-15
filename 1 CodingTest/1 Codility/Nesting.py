# Codility Lesson 7
# Detected time complexity:O(N)

def solution(S):

    stacker = list()
    for i in range(len(S)):
        stacker.append(S[i])
        
        if len(stacker) >= 2:
            if stacker[-2] == "(" and stacker[-1] == ")":
                stacker.pop()
                stacker.pop()

    if stacker:
        return 0
    else: # success, also empty S
        return 1 