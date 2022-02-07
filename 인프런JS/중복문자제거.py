data = input()
answer = []
for i in data:
    if i in answer:
        continue
    else:
        answer.append(i)
print(''.join(answer))
