def find_fibonacci(nthnumber:int):
    if nthnumber <= 1:
        return nthnumber
    else:
        return find_fibonacci(nthnumber - 1) + find_fibonacci(nthnumber - 2)

number_of_term = int(input("Enter number of term to print: "))
nthnumber = find_fibonacci(number_of_term)
print(nthnumber)