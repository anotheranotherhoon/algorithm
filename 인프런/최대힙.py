import sys
import heapq as hq
#sys.stdin=open("input.txt", "r")
a=[]
while True:
	n=int(input())
	if n==-1:
		break
	if n==0:
		if len(a)==0:
			print(-1)
		else:
			# 2. 부호를 반대로 해서 출력함
			print(-hq.heappop(a))
	else:
		# 1.부호를 반대로 해서 최소 힙으로 넣은 다음에
		hq.heappush(a, -n)