# Lesson 10, Prime and composite numbers
# O(sqrt(N))

def solution(N):
  
    i = 1
    minPerimeter = int(1e10) # enough?
    while i * i < N:
        if N % i == 0:
            minPerimeter = min(minPerimeter, 2 * (i + N//i) )
        i += 1

    if i * i == N:
        minPerimeter = 4 * i
        
    return minPerimeter