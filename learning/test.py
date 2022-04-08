from glob import glob
filename_list = glob('*.in')
with open(filename_list[0]) as f:
    N, lst = f.readlines()
    lst = sorted(list(map(int, lst.split())))
N = int(N)
a = [0] * (N+1)
a[1] = 10**5
for k in range(2, N+1):
    a[k] = min(a[k - 1], a[k - 2]) + lst[k-1] - lst[k-2]

with open('result.txt', 'w') as file:
    file.write(str(a[N]))