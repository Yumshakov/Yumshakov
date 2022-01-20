n, k, a, b = map(int, input().split())
res_list = []
res = a//b
res_1 = res + res//n
res_list.append(res_1)
res = a//b
res_2 = res + res//(k-1)
res_list.append(res_2)
print(max(res_list))