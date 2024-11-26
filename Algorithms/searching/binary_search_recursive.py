def binary_search_recursive(arr, target):
    counter = 0
    while len(arr) > 0:
        counter += 1
        mid = len(arr)//2
        if arr[mid] == target:
            return True, counter
        if arr[mid] < target:
            return binary_search_recursive(arr[(mid+1):], target)
        if arr[mid] > target:
            return binary_search_recursive(arr[:mid], target)
    return False, counter

array = [1,2,3,4,5,6,7,8,9,10]
array2 = [n**2 for n in array if n%2 == 0]
results = binary_search_recursive(array2, 100)
print(results)
print(array2)