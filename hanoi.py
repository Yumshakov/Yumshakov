def hanoi(n, i=1, k=3):
    tmp = 6 - i - k
    if n == 1:
        print(f'{i} - {k}')
        return
    else:
        hanoi(n-1, i, tmp)
        print(f'{i} - {k}')
        hanoi(n-1, tmp, k)

hanoi(3)