from collections import deque

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    board = [list(map(int, input().split())) for _ in range(m)]

    # 상 우상 우 우하 하 좌하 좌 좌상
    # 8방향 탐색을 위해
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    # 속도가 빠른 디큐를 사용
    Q = deque()
    cnt = 0
    for i in range(m):
        for j in range(n):
            # 먼저 육지인 곳을 찾는다.
            if board[i][j] == 1:
                # 육지를 q에 넣어주고
                Q.append((i, j))
                # 방문했다는 표시로 값을 2로 바꿔준다.
                board[i][j] = 0

                while Q:
                    # 현재 위치를 q에서 꺼내주고
                    tmp = Q.popleft()
                    # 8방향 탐색을 해준다.
                    for k in range(8):
                        xx = tmp[0] + dx[k]
                        yy = tmp[1] + dy[k]
                        # 전체 배열 범위 안에 있으면서
                        if 0 <= xx < m and 0 <= yy < n:
                            # 육지이면 값을 2로 바꿔주고 q에 넣어준다.
                            if board[xx][yy] == 1:
                                Q.append((xx, yy))
                                board[xx][yy] = 0

                # 이어져 있는 육지를 다 돌았다면 cnt+1
                else:
                    cnt += 1

    print(cnt)
