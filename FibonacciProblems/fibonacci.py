# // This is a for loop approach to print n first fibonacci terms. 

n = int(input("Enter a number of fibo terms: "))

previous_2nd = 0
previous_1st = 1

for i in range(n):
    print(previous_2nd, end=" ")
    next = previous_2nd + previous_1st
    previous_2nd = previous_1st
    previous_1st = next
