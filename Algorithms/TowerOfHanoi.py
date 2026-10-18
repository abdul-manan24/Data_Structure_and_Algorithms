def tower(N, A, B, C):
    if N == 1:
        print(A + " --> " + C)
        return
    tower(N-1, A, C, B)
    print(A + " --> " + C)
    tower(N-1, B, A, C)
    return 

tower(2, 'A', 'B', 'C')