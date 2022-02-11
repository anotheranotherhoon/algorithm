n = int(input())
data = list(map(int, input().split()))

for i in range(n):
    if i == 0:
        print(data[i], end=' ')
    elif data[i] > data[i-1]:
        print(data[i], end=' ')
