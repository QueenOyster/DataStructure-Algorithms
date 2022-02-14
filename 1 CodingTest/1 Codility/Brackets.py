# Lesson 7
# 100%, O(N)

from collections import deque

def solution(S):
    S = deque(S)
    stacker = deque()
    while S:
        current = S.popleft()
        if stacker: 
            if stacker[-1] == "(" and current == ")":
                stacker.pop()
            elif stacker[-1] == "{" and current == "}":
                stacker.pop()
            elif stacker[-1] == "[" and current == "]":
                stacker.pop()
            else:
                stacker.append(current)
        else:
            stacker.append(current)
    if stacker:
        return 0
    else:
        return 1