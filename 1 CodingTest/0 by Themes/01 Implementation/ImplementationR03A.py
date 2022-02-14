import sys
sys.stdin = open('input.txt', 'rt')
n, k = map(int, input().split())
cards = list(map(int, input().split()))
res = set() # 처음부터 set으로 받는 것이 안전
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n): # k 쓰지 말것!
            res.add(cards[i] + cards[j] + cards[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])
