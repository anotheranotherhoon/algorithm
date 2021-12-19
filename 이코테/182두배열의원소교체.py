n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
for i in range(k):
	if a[i]<b[i]:
		a[i], b[i]=b[i], a[i]
	# a[i] 원소가 b[i]원소 보다 작을 때 다음 인덱스로 간다.
	else:
		break
print (sum(a))
