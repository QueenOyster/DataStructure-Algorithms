n = 1260

cnt = 0
while n != 0:
    if n//500 >= 1:
        n -= 500
        cnt += 1
    elif n//100 >= 1:
        n -= 100
        cnt += 1
    elif n//50 >= 1:
        n -= 50
        cnt += 1
    elif n//10 >= 1:
        n -= 10
        cnt += 1
print(cnt)