n = int(input())
result = []
for i in range(n):
    num = int(input())
    if num == 0:
        result.pop()
    else:
        result.append(num)
print(sum(result))
