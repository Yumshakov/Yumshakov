string_text = ''
simple_qu = []
result_list = []
while True:
    string_text = input()
    if string_text[0:4] == 'push':
        simple_qu.append(string_text[5])
        result_list.append('ok')
    elif string_text == 'pop':
        result_list.append(simple_qu.pop(0))
    elif string_text == 'front':
        result_list.append(simple_qu[0])
    elif string_text == 'size':
        result_list.append(len(simple_qu))
    elif string_text == 'clear':
        simple_qu.clear()
        result_list.append('ok')
    elif string_text == 'exit':
        result_list.append('bye')
        break
for elem in result_list:
    print(elem)


