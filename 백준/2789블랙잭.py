n, m = map(int, input().split())
data = list(map(int, input().split()))
list = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if data[i] + data[j] + data[k] <= m:
                list.append(data[i] + data[j] + data[k])
result = max(list)
print(result)