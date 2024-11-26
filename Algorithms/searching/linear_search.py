def linear_search(arr, target):
    counter = 0
    for i in range(0, len(arr)):
        counter += 1
        if arr[i] == target:
            return i, counter
    return f"not found {counter}"

array = [1,2,3,4,5,6,7,8,9,10]
results = linear_search(array, 80)
print(results)
