# 문자열뒤집기
# 이것이코딩테스트다, p.313

import sys
sys.stdin = open('Greedy12.txt', 'rt')
s = input()
s = s + "2"

cnt_zero = 0
cnt_one = 0
now = int(s[0])
for i in range(1, len(s)):
    if int(s[i]) == now:
        continue
    else:
        if int(s[i-1]) == 0:
            cnt_zero += 1
            now = 1
        else:
            cnt_one += 1
            now = 0

print(min(cnt_zero, cnt_one))