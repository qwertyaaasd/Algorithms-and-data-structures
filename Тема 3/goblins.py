import sys
from collections import deque

n = int(input())

commands = []
for line in sys.stdin:
    commands.append(line.split())

left = deque()
right = deque()

for el in commands:
    if el[0] == '+':
        right.append(int(el[1]))
    elif el[0] == '*':
        left.append(int(el[1]))
    elif el[0] == '-':
        if left != deque():
            print(left.popleft())
        else:
            print(right.popleft())

    if len(left) < len(right):
        left.append(right.popleft())
    elif len(left) > len(right) + 1:
        right.appendleft(left.pop())