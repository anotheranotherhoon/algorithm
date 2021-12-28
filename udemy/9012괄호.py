T = int(input())

for _ in range(T):
	check = input()
	data = list(check)
	sum = 0

	for i in range(data):
		if i =="(":
			sum += 1
		elif i == ")":
			sum -=1
		if sum < 0:
			print("NO")
			break

if sum > 0:
	print("NO")
elif sum == 0:
	print("YES")

