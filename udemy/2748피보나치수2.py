# def f(n):
#     if n == 0:
#         return 0
#     elif n ==1:
#         return 1
#     return f(n - 1) + f(n -2)
# print(f(int(input())))
# 너무 오래 걸림

cache = [-1] * 91
cache[0] = 0
cache[1] = 1


def f(n):
    if cache[n] == -1:
        cache[n] = f(n - 1) + f(n -2)
    return cache[n]
print(f(int(input())))


# N = int(input())
# cache = [-1] * 91
# cache[0] = 0
# cache[1] = 1
# for i in range(2, N + 1 ):
#       cache[i] = cache[i - 1] + cache[i - 2]
# print(cache[N])