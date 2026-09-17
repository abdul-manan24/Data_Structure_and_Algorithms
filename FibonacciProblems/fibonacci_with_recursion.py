count = 2
def fibonacci(previous_1st, previous_2nd):
    global count
    if count <= 13:
        print(previous_2nd)
        next = previous_2nd + previous_1st
        previous_2nd = previous_1st
        previous_1st = next
        count += 1
        fibonacci(previous_1st, previous_2nd)
    return 

fibonacci(1, 0)