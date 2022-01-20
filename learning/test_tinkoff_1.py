len_array = int(input())
array = list(map(int, input().split()))
array_copy = array.copy()
for i in range(len_array-1):
    if array[i] >= array[i+1]:
        if -array[i] <= array[i+1]:
            array[i] = -array[i]
    elif abs(array[i]) <= array[i+1]:
        array[i] = abs(array[i])
array_new = sorted(array)

if array_new == array:
    print('Yes')
    print(*array)
else:
    print('No')
    print(*array_copy)