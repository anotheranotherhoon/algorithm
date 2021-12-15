INF=int(1e9) # 무한을 의미하는 값으로 10억을 설정

#노드의 개수 및 간선의 개수를 입력받음
n,m=map(int,input().split())

#2차원 리스트 값을 무한으로초기화
graph=[[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for a in range(1, n+1):
	for b in range(1, n+1):
		if a == b:
			graph[a][b]=0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(1, n+1):
	a, b = map(int, input().split())
	graph[a][b] = 1
	graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
	for a in range(1, n+1):
		for b in range(1, n+1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
	print("-1")
else:
	print(distance)
