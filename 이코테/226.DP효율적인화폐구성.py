# n,m = 2, 15 라고 가정해보자
n, m = map(int, input().split())


array = []
for i in range(n):
	array.append(int(input()))
#array=[2, 3]

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
	# i = 0, j = 2 // range(2, 16)<< 까지 돈다.
	# i = 0, j = 3
	# i = 0, j = 4 
	for j in range(array[i], m+1):
		# d[2-2] = 0
		# d[3-2] = 10001 이므로 바로 j = 4로 넘어간다.
		# d[4-2] = 1
		if d[j-array[i]] != 10001:
			# d[2] = min(d[2]=10001, d[2-2] + 1 = 0 + 1 ) = 1 따라서 d[2]=1
			# d[4] = min(d[4], d[4-2] + 1) = 2 따라서 d[4] = 2
			d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
	print(-1)
else:
	print(d[m])