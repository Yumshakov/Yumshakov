key_dict = {'a': 0,
            'b': 0,
            'c': 0}
lst = []
while len(lst) < 3:
  lst.append(input())

for elem in lst:
  if elem[1] == '>':
    key_dict[elem[0]] += 1
  elif elem[1] == '<':
    key_dict[elem[2]] += 1
  else:
     key_dict[elem[0]] += 1
     key_dict[elem[2]] += 1
sort_lst = sorted(key_dict.items(), key=lambda x: x[1])
for elem in sort_lst:
  print (elem[0], end='')
