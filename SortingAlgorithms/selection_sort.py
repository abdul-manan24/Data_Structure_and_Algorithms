# Implementation of selection sort.

sample_array = list(map(int, input().split()))
length_of_array = len(sample_array)
smallest_number_index = 0

for i in range(length_of_array):
    for j in range(i, length_of_array):
        if sample_array[j] < sample_array[smallest_number_index]:
            smallest_number_index = j
            smallest_number = sample_array.pop(sample_array[smallest_number_index])
    sample_array.insert(i, smallest_number)

print(sample_array)