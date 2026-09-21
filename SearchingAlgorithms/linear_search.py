# Implementation of linear search algorithm in python.

def linear_search(array:list, value_to_search):

    for i in range(len(array)):
        if array[i] == value_to_search:
            print(f"Value found at index {i}")
            return
    else:
        print("Value not found")
        return

array = list(map(int, input("Enter array: ").split()))
value_to_search = int(input("Enter value to search: "))

linear_search(array, value_to_search)