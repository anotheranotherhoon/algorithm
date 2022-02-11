n=int(input())
arr1 = list(map(int, input().split()))
m=int(input())
arr2 = list(map(int, input().split()))
p1=0
p2=0
answer = []
while(p1<n and p2<m):
    if arr1[p1]<=arr2[p2]:
        answer.append(arr1[p1])
        p1+=1
    else:
        answer.append(arr2[p2])
        p2+=1

while p1 < n:
    answer.append(arr1[p1])
    p1 += 1
while p2 < m:
    answer.append(arr2[p2])
    p2 += 1

print(answer)