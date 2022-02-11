from re import T


n, m = map(int, input().split())
data = list(map(int, input().split()))
tmp=set()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            tmp.add(data[i]+data[j]+data[k])
result = list(tmp)
result.sort(reverse=True)

print(result[m-1])