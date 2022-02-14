import sys
sys.stdin = open('input.txt', 'rt')
n =int(input())
student_list = list()

for _ in range(n):
    data = input().split()
    student_list.append((data[0], int(data[1])))
student_list.sort(key= lambda x: x[1])

for data in student_list:
    print(data[0], end=' ')