import fileinput
from collections import deque

lines = [line for line in fileinput.input()]

stacks = [deque() for _ in range(99999)]

x = 5

for x, line in enumerate(lines):
    if line[1] == '1':
        break
    for i,j in enumerate(range(1, len(line), 4), start=1):
        if line[j].strip():
            stacks[i].append(line[j])

l = len(lines[x].strip().split())

for i in range(x+2, len(lines)):
    line = lines[i].strip().split()
    amnt, fro, to = map(int, (line[1], line[3], line[5]))
    for j in range(amnt):
        stacks[to].appendleft(stacks[fro].popleft())

for i in range(1, l+1):
    print(stacks[i][0], end='')
print()