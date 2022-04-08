input_str = input()
#input_str = [elem for elem in input_str if elem in ['[', ']', '(', ')', '{', '}']]
stek_lst = []
index_story = []
for index, elem in enumerate(input_str):
    if elem in ['[', '{', '(']:
        stek_lst.append(elem)
        index_story.append(index+1)
    else:
        if elem == ']':
            if '[' in stek_lst:
                stek_lst.pop()
                index_story.pop()
            else:
                stek_lst.append(elem)
                index_story.append(index + 1)
                break
        elif elem == ')':
            if '(' in stek_lst:
                stek_lst.pop()
                index_story.pop()
            else:
                stek_lst.append(elem)
                index_story.append(index + 1)
                break
        elif elem == '}':
            if '{' in stek_lst:
                stek_lst.pop()
                index_story.pop()
            else:
                stek_lst.append(elem)
                index_story.append(index + 1)
                break
stek_lst = list(set(stek_lst))
if not stek_lst:
    print('Success')
else:
    if len(stek_lst) == 1:
        if stek_lst[0] in ['}',')',']']:
            print(index_story[0])
        elif stek_lst[0] in ['{','(','[']:
            print(index_story[0])
        else:
            print(stek_lst.index(stek_lst[0]) + 1)
    else:
        print(index_story[-1])
print(stek_lst, index_story, input_str)