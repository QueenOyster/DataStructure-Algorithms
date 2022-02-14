# Codility Lesson 2, OddOccurrencesInArray

def solution(A):
    counter_dict = dict()

    for item in A:
        if item not in counter_dict.keys():
            counter_dict[item] = 1
        else:
            counter_dict[item] += 1
    
    for key in counter_dict:
        if counter_dict[key] % 2 == 1:
            return key