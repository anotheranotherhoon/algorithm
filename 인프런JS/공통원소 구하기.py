n =  int(input())
data1 = list(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))
data1.sort()
data2.sort()
answer=[]
if n<=m:
    for i in range(n):
        for j in range(m):
            if data1[i]==data2[j]:
                answer.append(data1[i])
                break
else:
    for i in range(m):
        for j in range(n):
            if data2[i]==data1[j]:
                answer.append(data2[i])
                break

for i in answer:
    print(i, end=' ')
