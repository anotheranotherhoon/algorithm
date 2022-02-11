n = int(input())
data = list(map(int, input().split()))
answer = 0
max = 0
for i in range(n):
    if i == 0:
        answer += 1
        max = data[i]
    elif data[i] > max:
        answer +=1
        max = data[i]

print(answer)