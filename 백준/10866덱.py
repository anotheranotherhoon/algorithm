import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
dq = deque()

for _ in range(n):
    data = list(input().split())
    if data[0] == "push_front":
        dq.appendleft(data[1])
    elif data[0] == "push_back":
        dq.append(data[1])
    elif data[0] == "pop_front":
        if len(dq)==0:
            print(-1)
        else:
            print(dq.popleft())
    elif data[0] == "pop_back":
        if len(dq)==0:
            print(-1)
        else:
            print(dq.pop())
    elif data[0] == "size":
        print(len(dq))
    elif data[0] == "empty":
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif data[0] == "front":
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0])
    elif data[0] == "back":
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])