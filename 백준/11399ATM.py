n = int(input())
data = list(map(int, input().split()))
time = 0
data.sort()
for i in range(n):
    for j in range(i+1):
        time += data[j]
print(time)