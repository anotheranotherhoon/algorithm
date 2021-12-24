# from sys import stdin
# n = int(stdin.readline())
# A = list(map(int, stdin.readline().split()))
# m = int(stdin.readline())
# B = list(map(int, stdin.readline().split()))
# result=[0]*m
# for i in range(n):
# 	for j in range(m):
# 		if A[i]==B[j]:
# 			result[j]+=1
# print(result)
# 위의 방법말고 이분탐색을 사용해보자


from sys import stdin
n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
B = list(map(int, stdin.readline().split()))

A.sort()

def binary(num, bound):
	start, end = 0, n
	while(start<=end):
		mid = (start+end)//2
		if bound == 0:
			if A[mid] < num:
				start = mid + 1
			else:
				end = mid
		else:
			if A[mid] <= num:
				start = mid + 1
			else:
				end = num