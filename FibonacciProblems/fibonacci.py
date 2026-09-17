# // This is a for loop approach to print n first fibonacci terms. 

n = int(input("Enter a number of fibo terms: "))

previous_first = 0
previous_second = 1

for i in range(n):
    print(previous_first, end=" ")
    next = previous_first + previous_second
    previous_first = previous_second
    previous_second = next
