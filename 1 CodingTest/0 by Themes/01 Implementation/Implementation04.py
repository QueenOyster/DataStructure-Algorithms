# 럭키 스트레이트
# 이것이 코딩테스트다, p.321

def lucky_straight(score):
    score = str(score)
    length = len(score)

    left_total = 0
    right_total = 0
    for i in range(length//2):
        left_total += int(score[i])
    for i in range(length//2, length):
        right_total += int(score[i])

    if left_total == right_total:
        print("LUCKY")
    else:
        print("READY")

lucky_straight(123402)
# lucky_straight(7755)