n=int(input())
data = list(input().split() for _ in range(n))
result = []

for i in range(n):
    if data[i] in result:
        continue
    else:
        result.append(data[i])

print(result[1])
