def selection_sort(array):
    sorted = []
    for i in range(0, len(array)):
        index_to_move = min_index(array)
        sorted.append(array.pop(index_to_move))
    return sorted

def min_index(array):
    min = 0
    for i in range(1, len(array)):
        if array[i] < array[min]:
            min = i
    return min

u = [6,4,2,6,8,2,1,6,7,8,9,5,4,3,2]
new = [i*1 for i in range(0, 50000)]

print(selection_sort(u))
print(selection_sort(new))