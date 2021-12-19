data=input()
numsum=0
alpha=[]

for i in data:
	if i.isalpha():
		alpha.append(i)
	else:
		numsum += int(i)

alpha.sort()

if numsum != 0:
	alpha.append(str(numsum))

print(''.join(alpha))

