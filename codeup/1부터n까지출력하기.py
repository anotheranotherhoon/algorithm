def solution(n):
    if n == 0:
        return
    else:
        solution(n-1)
        print(n)

n = int(input())
solution(n)