from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
board = [input() for _ in range(N)]

def is_valid_coord(x, y):
    return 0<= x < M and 0 <= y < N

def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = 1
    dq = deque()
    dq.append((0, 0, 1))
    while dq:
        x, y, d = dq.popleft()
        if x == M - 1 and y == N-1:
            return d
        nd = d + 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_valid_coord(nx, ny) and board[nx][ny] == '1' and not chk[nx][ny]:
                chk[nx][ny] = 1
                dq.append((nx, ny, nd))
    return -1


print(bfs())