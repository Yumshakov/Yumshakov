import sys

A = [line.strip() for line in sys.stdin]

for j in range(len(A) - 1, 0, -1):
    for i in range(0, j):
        if A[i + 1] + A[i] > A[i] + A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]

print("".join(A))