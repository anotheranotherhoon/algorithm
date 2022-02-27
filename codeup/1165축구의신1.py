def solution(n, m):
    while n < 90:
        n +=5
        m += 1
    return(m)

n, m = map(int,input().split())
print(solution(n,m))