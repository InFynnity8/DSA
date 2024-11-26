def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = []
    greater_than_pivot = []
    
    for value in arr[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)