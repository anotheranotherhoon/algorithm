for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
        for j in range(1, m):
            for i in range(m):
                if i == 0: left_