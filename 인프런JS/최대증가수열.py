n = int(input())
data = list(map(int, input().split()))
data.insert(0,0)
dy=[0]*(n+1)
dy[1] = 1
res = 0
for i in range(2, n+1):
    max=0
    # i 바로 앞 부터 1번 까지 (그렇니까 0을 넣음 두번째 요소로), 
    for j in range(i-1, 0, -1):
        if data[j] < data[i] and dy[j]>max:
            max=dy[j]
    dy[i] = max+1
    if dy[i]>res:
        res = dy[i]
print(res)