def DFS(L, sum, tsum):
    global result
    #만약 지금의 합과 앞으로 더할 합이 현재 최대값보다 작을 경우 리턴
    if sum+(total-tsum)<result:
        return
    if sum > c:
        return
    if L==n:
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L]) 


c, n = map(int, input().split())
a=[0]*n
result = -214700
for i in range(n):
    a[i] = int(input())
total = sum(a)

DFS(0,0,0)
print(result)