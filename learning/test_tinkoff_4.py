input_data = list(map(int, input().split()))
gurnal = input_data[1:]
max = max(gurnal)
min = min(gurnal)
for index in range(len(gurnal)):
    if gurnal[index] == max:
        gurnal[index] = min
print(*gurnal)
