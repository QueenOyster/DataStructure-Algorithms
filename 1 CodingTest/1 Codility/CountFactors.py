def solution(N):
    checker = [0] * (1 + N//2)
    checker[0] = 1
    checker[1] = 1

    for i in range(2, N//2 + 1):
        k = 0
        while True:
            k += i
            if checker[k] == 0:
                checker[k] = 1
            if k + i <= N//2:
                continue
            else:
                break
    
    cnt = 0
    for element in checker:
        if element == 0:
            cnt += 1

    return cnt