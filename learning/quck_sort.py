list = list(map(int, input().split()))
def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
print(*quick_sort(list))
