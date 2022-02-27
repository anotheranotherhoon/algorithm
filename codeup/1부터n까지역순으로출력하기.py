def solution(n):
    if n ==0:
        return
    else:
        print(n)
        return solution(n-1)

n = int(input())
print(solution(n))