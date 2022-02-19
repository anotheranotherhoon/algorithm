dy = [0]* 30
dy[1] = 1
dy[2] = 2

for i in range(3, 8):
    dy[i] = dy[i-1] + dy[i-2]

print(dy)