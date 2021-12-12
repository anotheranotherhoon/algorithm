from collections import deque
import sys
input=sys.stdin.readline

dx=[1, 2, -1, -2, -2, -1, 1, 2]
dy=[2, 1, 2, 1, -1, -2, -2, -1]

t=int(input())

for i in range(t):
	n = int(input())
	cx, cy = map(int, input().split())
	fx, fy = map(int, input().split())
	board=[[0]*n for _ in range(n)]
	Q=deque()
	Q.append((cx, cy))
	dis=[[0]*n for _ in range(n)]
	while Q:
		tmp=Q.popleft()
		if tmp[0] == fx and tmp[1] == fy:
			break
		for i in range(8):
			xx=tmp[0]+dx[i]
			yy=tmp[1]+dy[i]
			if 0<=xx<n and 0<=yy<n and board[xx][yy]==0:
				dis[xx][yy]=dis[tmp[0]][tmp[1]]+1
				Q.append((xx, yy))

result=0
for i in range(n):
	for j in range(n):
		if dis[i][j]>result:
			result=dis[i][j]
print(result-1)
