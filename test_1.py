'''three_list = input().split()
parent_dict = {}

for i, parent in enumerate(three_list):
    if parent_dict.get(parent) == None:
        parent_dict[parent] = []
    parent_dict[parent].append(str(i))

print(parent_dict)'''

a = [1,2,3]
b = a
a=a+[4]
print((a==b)*b)