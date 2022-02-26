# Lesson 7
# O(N), 100%

# stack이 필요한 이유!
# 물고기 하나 vs 상류 (X)
# 하류 vs 상류 (O)

def solution(A, B):
    N = len(A)
    lives = len(A)
    fightMode = 0
    attacker = list()
    for i in range(N):
        if fightMode == 0:
            if B[i] == 0:
                pass
            elif B[i] == 1:
                attacker.append(A[i])
                fightMode = 1

        elif fightMode == 1:
            if B[i] == 0:
                while attacker:
                    if attacker[-1] < A[i]:
                        attacker.pop()
                        lives -= 1
                    else:
                        lives -= 1
                        break
                if not attacker:
                    fightMode = 0
            elif B[i] == 1:
                attacker.append(A[i])
    return lives