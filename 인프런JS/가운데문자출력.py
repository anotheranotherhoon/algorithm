data = input()
result = []
if len(data) % 2 == 0:
    result.append(data[len(data)//2-1])
    result.append(data[len(data)//2])
    answer = ''.join(result)
    print(answer)
else:
    result.append(data[len(data)//2])
    answer = ''.join(result)
    print(answer)