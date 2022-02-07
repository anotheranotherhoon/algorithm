data = input()
cnt = 0
for i in data:
    if 65<= ord(i) <= 90:
        cnt += 1
print(cnt)