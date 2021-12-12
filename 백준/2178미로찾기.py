import sys
from collections import deque
a, b = map(int,input().split())
dx=[-1,0,1,0]
dy=[0,1,0,-1]
board=[list(map(int, input().split())) for _ in range(a)]
dis=[[0]*b for _ in range(a)]
Q=deque()
Q.append((0,0))
board[0][0]=1
while Q:
	tmp=Q.popleft()
	for i in range(4):
		x=tmp[0]+dx[i]
		y=tmp[1]+dy[i]
		if 0<=x<a and 0<=y<b and board[x][y]==1:
			board[x][y]=1
			dis[x][y]=dis[tmp[0]][tmp[1]]+1
			Q.append((x,y))
print(dis[a][b])