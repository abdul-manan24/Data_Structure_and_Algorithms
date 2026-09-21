# Implementatio of counting sort algorithm.

def countingSort(array):
    if not array:
        return array

    max_value = max(array)
    count = [0] * (max_value + 1)

    for num in array:
        count[num] += 1

    array[:] = []

    for num, freq in enumerate(count):
        array.extend([num] * freq)

    return array

unsorted_array = list(map(int, input("Enter unsorted array: ").split()))
sorted_array = countingSort(unsorted_array)
print(f"sorted array: {sorted_array}")