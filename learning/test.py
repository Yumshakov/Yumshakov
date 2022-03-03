import sys
from functools import cmp_to_key

def cmp (x,y):
    if x + y > y + x:
        return -1
    elif x + y == y + x:
        return 0
    else:
        return 1

a = [i.rstrip() for i in sys.stdin]
a.sort(key=cmp_to_key(cmp))

print(*a, sep='')