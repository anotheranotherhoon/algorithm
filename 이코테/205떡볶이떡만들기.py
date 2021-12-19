n,m = list(map(int, input().split()))

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start<=end):
	total=0
	mid=(start+end)//2
	for x in array:
		if x > mid:
			total += x - mid
	if total < m:
		end = mid -1
	else:
		# result에 절단기 최대 높이를 기록함 만약에 답이라고 하면 while(start<=end)에서 참이 나와서 while문 탈출
		result = mid 
		start = mid + 1

print(result)