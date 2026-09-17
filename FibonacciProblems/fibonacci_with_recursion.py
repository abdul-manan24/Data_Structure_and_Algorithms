count = 2

def fibonacci(previous_1st, previous_2nd):
    global number_of_terms
    global count
    if count <= number_of_terms:
        print(previous_2nd, end=" ")
        next = previous_2nd + previous_1st
        previous_2nd = previous_1st
        previous_1st = next
        count += 1
        fibonacci(previous_1st, previous_2nd)
    return

number_of_terms = int(input("Enter number of terms to print: "))
fibonacci(1, 0)