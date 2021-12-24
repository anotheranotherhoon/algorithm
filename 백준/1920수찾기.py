n=int(input())
N=list(map(int, input().split()))
m=int(input())
M=list(map(int, input().split()))
list=[]

N.sort()

for i in M:
	left=0
	right=len(N)-1
	is_find=False
	while True:
		median = (left + right) // 2
		if i==M[median]:
			print(1)
			if_find = True
			break
		elif i>M[median]:
			left = median + 1
		elif i<M[median]:
			right = median - 1
		if left > right:
			break

		if not is_find:
			print(0)
		