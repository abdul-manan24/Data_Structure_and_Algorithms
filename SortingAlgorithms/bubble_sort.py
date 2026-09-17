# implementation of bubble sort algorithem.

sample_array = list(map(int, input().split()))


for i in range(len(sample_array) - 1):
    for j in range(len(sample_array) - i - 1):
        if sample_array[j] > sample_array[j+1]:
            sample_array[j], sample_array[j+1] = sample_array[j+1], sample_array[j]

print(sample_array)