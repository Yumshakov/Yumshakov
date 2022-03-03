from collections import deque

first = deque()
second = deque()

n = int(input())
for i in range(n):
    s = input().split()
    if s[0] == '-':
        print(first.popleft())
    elif s[0] == '+':
        second.append(s[1])
    else:
        second.appendleft(s[1])
    if len(second) > len(first):
        x = second.popleft()
        first.append(x)