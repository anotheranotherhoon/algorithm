n = int(input())
data = list(map(int, input().split()))
m = int(input())
dy = [1000]*(m)
dy[0] = 0
for i in range(n):
    for j in range(data[i], m+1):
        dy[j] = min(dy[j], dy[j-data[i]]+1)
print(dy[m])