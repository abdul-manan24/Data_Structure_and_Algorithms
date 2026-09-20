# Implementation of selection sort.

sample_array = list(map(int, input("Enter unsorted array: ").split()))
length_of_array = len(sample_array)


for i in range(length_of_array-1):
    smallest_number_index = i
    for j in range(i + 1, length_of_array):
        if sample_array[j] < sample_array[smallest_number_index]:
            smallest_number_index = j

    if smallest_number_index != i:
        sample_array[i], sample_array[smallest_number_index] = sample_array[smallest_number_index], sample_array[i]

print(f"Sorted array: {sample_array}")