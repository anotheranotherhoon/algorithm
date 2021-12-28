T = int(input())

for _ in range(T):
	main=[]
	isVPS = True
	for i in input():
		if i =="(":
			main.append(i)
		else:
			if main:
				main.pop()
			else:
				isVPS = False
				break
	if main:
		isVPS = False
	print('YES' if isVPS else 'NO')



