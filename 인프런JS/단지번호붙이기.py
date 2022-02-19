def DFS(x,y):
    global cnt
    cnt+=1
    #중복방문하지 않도록 0으로 만듬
    board[x][y]=0
    for i in range(4):
        xx= x+dx[i]
        yy= y+dy[i]
        if 0<=xx<=n and 0<=yy<=n and board[xx][yy]==1:
            DFS(xx, yy)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            #cnt를 0으로 만듦
            cnt=0
            DFS(i, j)
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)