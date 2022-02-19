def DFS(x, y):
    global cnt
    # 가장 높은 점에 도달하면 cnt 값을 하나 올린다.
    if x==ex and y==ey:
        cnt +=1
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            # 외벽을 넘어가면 안되고 방문한적이 없어야한다.
            if 0<=xx<=6 and 0<=yy<=6 and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
                ch[xx][yy]=1
                DFS(xx,yy)
                # 방문했던 체크를 푼다.
                ch[xx][yy]=0

# 타일의 갯수
n = int(input())
# [0,0,0,0,0]< 5번 반복 board and ch
board = [[0]*n for _ in range(n)]
# 방문했는지 체크
ch = [[0]*n for _ in range(n)]
max = -2147000000
min = 2147000000
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(n):
    # 한 줄 씩 들어옴
    tmp = list(map(int, input().split()))
    for j in range(n):
        # if else가 아니라 두 번다 수행해야함. 시작점과 끝점의 인덱스 값을 찾는다. 
        if tmp[j] < min:
            min = tmp[j]
            sx=i
            sy=j
        if tmp[j]>max:
            max = tmp[j]
            ex=i
            ey=j
        #board를 채운다.
        board[i][j]=tmp[j]
#시작지점의 좌표를 방문 표시함
ch[sx][sy]=1
cnt=0
#시작지점에서 DFS를 시작함
DFS(sx, sy)
print(cnt)

