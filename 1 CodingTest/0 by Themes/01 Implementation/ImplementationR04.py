import sys
import time
sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n = int(input())
scores = list(map(int, input().split()))
avg_score = round(sum(scores)/n)

score_gap = 2147000000
last_score = -2147000000
for idx, score in enumerate(scores):
    # 가까운 점수
    if score_gap > abs(score - avg_score): # 무리해서 합치지 말고, 먼저 분리해서 생각 하기
        score_gap = abs(score - avg_score)
        last_score = score
        idx_memory = idx + 1
    elif score_gap == abs(score - avg_score):
        if score > last_score:
            last_score = score
            idx_memory = idx + 1
print(avg_score, idx_memory)


end_time = time.time()
print('time: ', end_time - start_time)