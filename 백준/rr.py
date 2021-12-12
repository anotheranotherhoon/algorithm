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
 
    graph = [([0] * n) for i in range(n)]
 
    queue = deque()
    queue.append((cx, cy))
    graph[cx][cy] = 1
 
    while queue:
        x, y = queue.popleft()
        if x == fx and y == fy:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
 
    print(graph[fx][fy]-1)