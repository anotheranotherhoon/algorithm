n = int(input())
data = list(map(int, input().split()))
cnt = 0
result = 0
for i in range(n):
    if data[i] == 1:
        cnt += 1
        result += cnt
    else:
        cnt = 0

print(result)

