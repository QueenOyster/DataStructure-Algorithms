# Codility Lesson 6, Triangle
# time complexity: 

def solution(A):
	n = len(A)
	A.sort()
	result = 1
	for k in range(1, n):
		if A[k] != A[k-1]:
			result += 1
	return result