n = int(input())
data = []
for _ in range(n):
    s, e = map(int, input().split())
    data.append([s, e])
data = sorted(data, key=lambda a:a[0])
data = sorted(data, key=lambda a:a[1])
last = 0
cnt = 0
for i, j in data:
    if i > last:
        cnt += 1
        last = j
print(cnt)