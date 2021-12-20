n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
lt=0
rt=max(data)
result=0
while(lt<=rt):
	total=0
	mid = (lt+rt)//2
	for x in data:
		if x > mid:
			total += x-mid
	if total < m:
		rt = mid-1
	else:
		result = mid
		start = mid +1
print(result)
