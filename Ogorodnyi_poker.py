from collections import Counter
dict_combinatoins = {
    '23': 'Фулл Хаус',
    '32': 'Фулл Хаус',
    '3': 'Сет',
    '22': 'Две пары',
    '4': 'Каре',
    '5': 'Шулер',
    '2': 'Пара'
}
lst = sorted(input().split())
dict_count = dict(Counter(lst))
res_str = ''
count_diff = 0

for index_lst in range(1, len(lst)):
    diff = int(lst[index_lst]) - int(lst[index_lst-1])
    if diff == 1:
        count_diff += 1
    else:
        break
for val in dict_count.values():
    if val == 4:
        res_str += str(val)
    elif val == 2 or val == 3:
        res_str += str(val)
    elif val == 5:
        res_str += str(val)

if len(res_str):
    print(dict_combinatoins[res_str])
elif count_diff == 4:
    print('Стрит')
else:
    print('Старшая карта')
