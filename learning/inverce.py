mid_list = []
count_str = 0
cursor = 0
with open('inverse.in') as file:
    for line in file:
        mid_list.append(line.strip().split())
    mid_list = list(map(int, mid_list[1]))
len_list = len(mid_list)
while cursor < len_list:
    for elem in mid_list[cursor+1:]:
        if mid_list[cursor] > elem:
            count_str += 1
    cursor += 1
with open ('inverse.out', 'w') as file:
    file.write(str(count_str))
