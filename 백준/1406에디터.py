from collections import deque


data = list(input())
n = int(input())
command = deque()
cursor = len(data)
for _ in range(n):
    command.append(input().split())

while command:
    x = command.popleft()
    if x[0] == "L":
        if not cursor == 0:
            cursor -= 1
        else:
            continue
    elif x[0] == "D":
        if not cursor == len(data):
            cursor += 1
        else:
            continue
    elif x[0] == "B":
        if not cursor == 0:
            data = data[0:cursor-1] + data[cursor:0]
        else:
            continue
    elif x[0] == "P":
        data = data[0:cursor-1] + x[1] + data[cursor:]
print(data)



