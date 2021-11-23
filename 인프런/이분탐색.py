n, m = map(int, input().split())
a=list(map(int,input().split()))
a.sort()
lt=0
rt=n-1
while li <=rt:
	mid=(lt+rt)//2
	if a[mid]==m:
		print(mid+1)
	elif a[mid]>m:
		rt=mid-1
	else:
		li=mid+1