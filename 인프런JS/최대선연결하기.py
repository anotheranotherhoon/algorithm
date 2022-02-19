n = int(input())
data = list(map(int, input().split()))
data.insert(0,0)
dy = [0]*(n+1)
dy[1] = 1
res = 0
for i in range(n+1):
    max = 0
    for j in range(i-1,0)
    if data[j] <data[i] and dy[j]>max:
        max =dy[j]
    dy[i] = max+1
    if dy[i]>res:
        res = dy[i]
print(res)
