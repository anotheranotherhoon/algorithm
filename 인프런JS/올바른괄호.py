data=input()
result=[]
answer="YES"
for i in data:
    if i=="(":
        result.append(i)
    elif len(result) == 0 and i==")":
        answer = "NO"
        break
    else:
        result.pop()

if len(result) != 0:
    answer="NO"

print(answer)
