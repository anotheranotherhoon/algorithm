def DFS(L, sum):
    global cnt
    # 동전의 가짓수와 같을 때
    if L==k:
        # 합이 지폐의 금액과 같을 때
        if sum==t:
            cnt += 1
    else:
        #각 동전의 갯수 만큼 돌아야하므로 cn[L] + 1 해준다.
        for i in range(cn[L]+1):
            #DFS가 각 동전의 갯수 만큼 보기에서는 3번2번5번 만큼 실행됨 또 그안에서 다음 동전의 갯수만큼 퍼짐
            DFS(L+1, sum+(cv[L])*i)

t=int(input())
k=int(input())
cv=[]
cn=[]
for i in range(k):
    a, b = map(int, input().split())
    cv.append(a)
    cn.append(b)
cnt= 0
DFS(0, 0)
print(cnt)