phone_cod = {2:'abc',
             3:'def',
             4:'ghi',
             5:'jkl',
             6:'mno',
             7:'pqrs',
             8:'tuv',
             9:'wxyz'}

n = int(input())
ministerstvo_list = [input() for i in range(n)]
result_list = []
result_string = ''
for elem in ministerstvo_list:
    for letter in elem:
        for k, v in phone_cod.items():
            if letter in v:
                result_string += str(k)
    result_list.append(result_string)
    result_string = ''
print(len(set(result_list)))
