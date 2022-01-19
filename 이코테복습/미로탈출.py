from collections import deque

# n, m 을 공백으로 구분하여 입력받기 
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if xx < 0 or yy < 0 or xx >= n or yy >= m:
                continue
            # 벽인 경우 무시
            if graph[xx][yy] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[xx][yy] == 1:
                graph[xx][yy] = graph[x][y] + 1
                queue.append((xx, yy))
    # 가장 오른쪽 아래까지의 최단 거리 반환            
    return graph[n - 1][m - 1]

print(bfs(0, 0))
