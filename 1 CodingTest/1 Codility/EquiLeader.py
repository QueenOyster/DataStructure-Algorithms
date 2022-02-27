# Lesson 8, Leader
# O(N), 100%

def solution(A):
    
    rightDict = dict()
    for element in A:
        try:
            rightDict[element] += 1
        except:
            rightDict[element] = 1

    leftDict = dict()
    leftLeader = None
    leftLeaderCount = 0
    equiLeaderCount = 0
    for idx, element in enumerate(A):
        rightDict[element] -= 1
        try:
            leftDict[element] += 1
        except:
            leftDict[element] = 1

        # get leftLeader
        if leftDict[element] > leftLeaderCount:
            leftLeaderCount = leftDict[element]
            leftLeader = element
        
        # get equiLeader
        if leftDict[leftLeader] > (idx+1)//2 and rightDict[leftLeader] > (len(A)-(idx+1))//2:
            equiLeaderCount += 1
    return equiLeaderCount


# 22%
import heapq
def solution(A):

    rightDict = dict()
    for item in A:
        try:
            rightDict[item] += 1
        except:
            rightDict[item] = 1

    rightHeapq = list()
    for key, value in rightDict.items():
        heapq.heappush(rightHeapq, [-value, key])

    equileader = 0
    leftHeapq = list()
    for i in range(len(A)-1):
        for item in rightHeapq:
            if item[1] == A[i]:
                item[0] += 1
                break

        for item in leftHeapq:
            if item[1] == A[i]:
                item[0] -= 1
                break
        else:
            heapq.heappush(leftHeapq, [-1, A[i]])
    
        # print(i)
        # print(leftHeapq)
        # print(heapq.nsmallest(1, leftHeapq))
        # print(rightHeapq)
        # print(heapq.nsmallest(1, rightHeapq))

        if abs(heapq.nsmallest(1, rightHeapq)[0][0]) > len(rightHeapq)/2 and abs(heapq.nsmallest(1, leftHeapq)[0][0]) > len(leftHeapq)/2:
            if (heapq.nsmallest(1, rightHeapq))[0][1] == (heapq.nsmallest(1, leftHeapq))[0][1]:
                equileader += 1
    return equileader