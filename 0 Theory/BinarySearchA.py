import random
raw_data_list = random.sample(range(100), 10)
print("raw_data_list: ", raw_data_list)
raw_data_list.sort()
print("sorted_data_list: ", raw_data_list)


def binary_search(data, search):
    print("current data: ", data)
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0: # Defensive Coding
        return False
    
    medium = len(data) // 2
    if search == data[medium]:
        return True
    else: # medium+1을 하면 len==2일때 out of range되어버림.
        if search >= data[medium]:
            return binary_search(data[medium:], search)
        else:
            return binary_search(data[:medium], search)


print("binary_search(81)")
print(binary_search(raw_data_list, 81))