data = input()
zero=0
one=0

if data[0] == '1':
	one += 1
else:
	zero += 1

for i in range(len(data)-1):
	if data[i] != data[i+1]:
		if data[i+1] == '1':
			one += 1
		else:
			zero +=1

print(min(zero, one))
