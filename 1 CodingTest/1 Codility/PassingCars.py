# Codility Lesson 5, PassingCars
# time complexity: O(N)
# pair? -> "https://www.google.com/search?q=pair&newwindow=1&source=lnms&tbm=isch&sa=X&ved=2ahUKEwisvoi39e71AhWU4mEKHeEMDzkQ_AUoAXoECAEQAw&biw=1745&bih=881&dpr=1.1"

max_number = int(1e9)

def solution(A):
    
    P_count = 0
    pairs_detected = 0
    for direct_integer in A:
        if direct_integer == 0: # P detected
            P_count += 1
        else: # Q detected
            pairs_detected += P_count
            if pairs_detected > max_number:
                return -1
                
    return pairs_detected