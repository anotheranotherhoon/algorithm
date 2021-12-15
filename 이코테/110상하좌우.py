a=int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types =['L', 'R', 'U', 'D']

for plan in plans:
	for i in range(len(move_types)):
		if plan == move_types[i]:
			xx = x + dx[i]
			yy = y + dy[i]
	if 1<=xx<=a and 1<=yy<=a:
		x, y = xx, yy

print(x, y)