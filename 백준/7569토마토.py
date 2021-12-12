from collections import deque
dx=[1, 0 , -1, 0, 0, 0]
dy=[0, 1, 0, -1, 3, -3]
m, n, h = map(int,input().split())
board=[list(map(int, input().split())) for _ in range(n*h)]
dis=[[0]*m for _ in range(n*h)]
Q=deque()
for i in range(m):
	for j in range(n*h):
		if board[i][j]==1:
			Q.append((i ,j))

while Q:
	for i in range(6):
		tmp=Q.poplef()
		xx=tmp[0]+dx[i]
		yy=tmp[1]+dy[j]
		if 0<=xx<m and 0<=yy<n*h and board[xx][yy]==0:
			board[xx][yy]=1
			Q.append(xx,yy)
			dis[xx][yy]=dix[tmp[0]][tmp[1]]+1

flag=1
for i in range(m):
	for j in range(n*h):
		if board[i][j]==0:
			flag=0
result=0
if flag==1:
	for i in range(m):
		for j in range(n*h):
			if dis[i][j]>result:
				result=dix[i][j]
	print(result)
else:
	print(-1)
	
