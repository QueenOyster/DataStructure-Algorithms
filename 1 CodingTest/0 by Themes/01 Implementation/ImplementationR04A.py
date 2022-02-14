import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
scores = list(map(int, input().split()))
ave = round(sum(scores) / n)

min = 2147000000 # 정수형 크기의 가장 큰 값(4byte)
for idx, score in enumerate(scores):
    tmp = abs(score - ave)
    if tmp < min:
        min = tmp
        score_memory = score
        idx_memory = idx + 1
    elif tmp == min:
        if score > score_memory: # = 넣으면 맨 뒤의 값
            score_memory = score
            idx_memory = idx + 1
print(ave, idx_memory)