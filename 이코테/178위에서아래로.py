a=int(input())
array=[]
for i in range(a):
	array.append(input())

array = sorted(array, reverse=True)

for i in array:
	print(i, end=" ")