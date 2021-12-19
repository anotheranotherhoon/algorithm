a=input()
length =len(a)
sum=0

for i in range(length//2):
	sum += int(a[i])

for i in range(length//2, length):
	sum -= int(a[i])

if sum==0:
	print("LUCKY")
else:
	print("READY")