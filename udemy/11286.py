# import heapq as hq
# import sys
# input = sys.stdin.readline
# pq = []
# for _ in range(int(input())):
# 	x = int(input())
# 	if x:
# 		hq.heappush(pq, (abs(x), x))
# 	else:
# 		print(hq.heappop(pq) if pq else 0)
# 			# 위의 코드는 아래 코드를 의미한다.
# 			# if pq:
# 			# 	print(hq.heappop(pq))
# 			# else:
# 			# 	print(0)

import heapq as hq
import sys
input = sys.stdin.readline
min_heap = [] # 양수
max_heap = [] # 음수
for _ in range(int(input())):
	x = int(input())
	if x:
		if x > 0:
			hq.heappush(min_heap, x)
		else:
			hq.heappush(max_heap, -x)
	else:
		if min_heap:
			if max_heap:
				if min_heap[0] < abs(max_heap[0]):
					print(hq.heappop(min_heap))
				else:
					print(-hq.heappop(max_heap))
			else:
				print(hq.heappop(min_heap))
		else:
			if max_heap:
				print(-hq.heappop(max_heap))
			else:
				print(0)
