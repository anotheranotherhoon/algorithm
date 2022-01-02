import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: x - 1, map(int, input().split()))
    adj[a][b] = adj[b][a] = 1

ans = 0
chk = [0] * N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] == 0 and chk[nxt] == 0:
            chk[nxt] = 1
            dfs(nxt)

for i in range(N):
    if chk[i] == 0:
        ans += 1
        chk[i] = 1
        dfs(i)

print(ans)