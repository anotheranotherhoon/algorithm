n, m = map(int, input().split())
data = [list(map(int, input().split()))for _ in range(n)]
data.sort(key=lambda x:x[0])
money=0
for i in range(n):
    money = m-(data[i][0]/2 + data[i][1])
    cnt = 1
    for j in range(i):
        if j!=i and (data[j][0] + data[j][1]) > money:
            break
        if j!=i and (data[j][0] + data[j][1]) <= money:
            money-= (data[j][0] + data[j][1])
            cnt += 1
print(cnt)