from  collections import deque
import sys
input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


t = int(input())

for i in range(t):
    n = int(input())
    cx, cy = map(int, input().split()) 
    fx, fy = map(int, input().split())
    board = [([0] * n) for i in range(n)]
    Q = deque()
    Q.append((cx, cy))
    board[cx][cy] = 1
    while Q:
        tmp = Q.popleft
        if tmp[0] == fx and tmp[1] == fy:
            break
        for i in range(8):
            xx = tmp[0] + dx[i]
            yy = tmp[1] + dy[i]
            if 0<=xx<n and 0<=yy<n and board[xx][yy] == 0:
                board[xx][yy] = board[tmp[[0]]][tmp[1]] + 1
                Q.append((xx, yy))
    print(board[fx][fy]-1)