n=int(input())

count = 0
for i in range(n+1):
	# 시계는 59분에서 0분으로 이동하므로 초도 마찬가지
	for j in range(60):
		for k in range(60):
			if '3' in str(i) + str(j) + str(k):
				count+=1
print(count)