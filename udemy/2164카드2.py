# from collections import deque
# N = int(input())
# data = deque(range(1, N+1))

# while len(data)>1:
# 	data.popleft()
# 	data.append(data.popleft())

# print(data.popleft())

N = int(input())
data=[]
for i in range(1, N+1):
	data.append(i)
while len(data) > 1:
	data.pop(0)
	data.append(data.pop(0))

print(data.pop())