import sys
sys.stdin = open('input.txt', 'rt')

def reverse(num):
    num = str(num)
    tmp = ''
    for idx in range(len(num)):
        tmp += num[len(num)-1 -idx]
    return int(tmp)

def isPrime(num):
    if num == 1:
        return False
    else: 
        for i in range(2, (num//2)+1):
            if num % i == 0: # factor of prime number: 1, itself
                return False
        else:
            return True
    
n = int(input())
numbers = list(map(int, input().split()))
for number in numbers:
    rev_number = reverse(number)
    if isPrime(rev_number) == True:
        print(rev_number, end=' ')