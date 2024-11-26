def binary_search(arr: any, target: any):
    first = 0
    last = len(arr) - 1
    counter = 0
    while first <= last:
        counter += 1
        mid = (first + last)//2
        if arr[mid] == target:
            return mid, counter
        if arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return f"not found {counter}"

array = [1,2,3,4,5,6,7,8,9,10]
results = binary_search(array, 1)
print(results)