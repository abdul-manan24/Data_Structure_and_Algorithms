# Implementation of binary search algorithm.

def binary_search(array:list, value_to_search):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == value_to_search:
            print(f"Value {value_to_search}, found at {mid}")
            return
        elif array[mid] > value_to_search:
            right = mid + 1
        else:
            left = mid - 1
    else:
        print(f"Value {value_to_search}, not found")

sorted_array = list(map(int, input("Enter sorted array: ").split()))
value_to_search = int(input("Enter the value to search: "))

binary_search(sorted_array, value_to_search)