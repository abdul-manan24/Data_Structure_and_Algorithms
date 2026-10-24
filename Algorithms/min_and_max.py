# Finding min and max value using divide and conquer.

def min_and_max(arr):
    min = int()
    max = int()
    if len(arr) == 2:
        if arr[0] > arr[1]:
            max = arr[0] 
            min = arr[1]
        else:
            max = arr[1] 
            min = arr[0]

        return

    mid = 0 + len(arr) // 2

    min_and_max(arr[:mid])
    min_and_max(arr[mid:])

    return min, max

arr = list(map(int, input("Enter list: ").split()))
print("Min and max: ", min_and_max(arr))