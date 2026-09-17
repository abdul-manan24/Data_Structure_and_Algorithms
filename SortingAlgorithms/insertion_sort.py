# implementation of insertion sort algorithm.

sample_array = list(map(int, input().split()))
length = len(sample_array)

for i in range(1, length):
    insert_index = i
    current_value = sample_array.pop(i)
    for j in range(i-1, -1, -1):
        if sample_array[j] > current_value:
            insert_index = j
    sample_array.insert(insert_index, current_value)

print(sample_array)