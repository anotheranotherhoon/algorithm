a = input()
result = int(a[0])
for i in range(1, len(a)):
	num = int(a[i])
	if num <= 1 or result <= 1:
		result += num
	else:
		result *= num
print(result)

