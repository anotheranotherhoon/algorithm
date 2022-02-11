n = int(input())
data = list(map(int, input().split()))
cnt = 0
result = []
for i in range(n):
    for j in range(n):
        if data[i] <= data[j]:
            cnt +=1
    result.append(cnt)
    cnt = 0

for i in range(n):
    print(result[i], end=' ')