n = int(input())
data = []
for _ in range(n):
    data.append(input())
cnt = 0
result = ''
for i in range(len(data)):
    if len(data[i]) > cnt:
        cnt = len(data[i])
        result = data[i]

print(result)
