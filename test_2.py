input_str = input()
#input_str = [elem for elem in input_str if elem in ['[', ']', '(', ')', '{', '}']]
stek_lst = []
index_story = []
test_lst = ['}', ']', ')']
count = 0
for elem in test_lst:
    if elem in input_str:
        count += 1
if count:
    for index, elem in enumerate(input_str):
        if elem in ['[', '{', '(']:
            stek_lst.append(elem)
            index_story.append(index+1)
        else:
            if elem == ']':
                if stek_lst:
                    if '[' == stek_lst[-1]:
                        stek_lst.pop()
                        index_story.pop()
                    else:
                        stek_lst.append(elem)
                        index_story.append(index + 1)
                        break
                else:
                    stek_lst.append(elem)
                    index_story.append(index + 1)
                    break
            elif elem == ')':
                if stek_lst:
                    if '(' == stek_lst[-1]:
                        stek_lst.pop()
                        index_story.pop()
                    else:
                        stek_lst.append(elem)
                        index_story.append(index + 1)
                        break
                else:
                    stek_lst.append(elem)
                    index_story.append(index + 1)
                    break
            elif elem == '}':
                if stek_lst:
                    if '{' == stek_lst[-1]:
                        stek_lst.pop()
                        index_story.pop()
                    else:
                        stek_lst.append(elem)
                        index_story.append(index + 1)
                        break
                else:
                    stek_lst.append(elem)
                    index_story.append(index + 1)
                    break
    print('Success' if not stek_lst else index_story[-1])
else:
    print('1')
#print(stek_lst, index_story)

