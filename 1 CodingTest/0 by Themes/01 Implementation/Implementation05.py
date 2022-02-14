# 문자열 재정렬
# 이것이 코딩테스트다, p.322

def solution(s):

    arr = list()
    sum = 0
    flag = 0
    for i in range(len(s)):
        if s[i].isdigit():
            sum += int(s[i])
            flag = 1
        else:
            arr.append(s[i])

    arr.sort()
    result = ""
    for i in range(len(arr)):
        result += arr[i]

    if flag == 1:
        sum = str(sum)
        result += sum

    return result

print(solution('K1KA5CB7'))
print(solution("AJKDLSI412K4JSJ9D"))
print(solution('CBDEA'))