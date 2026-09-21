# Implementation of radix sort algorithm in pyhton.

sample_array = list(map(int, input("Enter unsorted array: ").split()))
print(f"Original array {sample_array}")
radix_array = [[],[],[],[],[],[],[],[],[],[]]
maxValue = max(sample_array)
exp = 1

while maxValue // exp > 0:

    while len(sample_array) > 0:
        value = sample_array.pop()
        radix_index = (value // exp) % 10
        radix_array[radix_index].append(value)

    for bucket in radix_array:
        while len(bucket) > 0:
            value = bucket.pop()
            sample_array.append(value)

    exp *= 10

print(f"Sorted Array: {sample_array}")