t=int(input())

zero=[1,1,1]

def pado(num):
	length=len(zero)
	if length <= num:
		for i in range(length,num):
			zero.append(zero[i-3]+zero[i-2])
	print(zero[num-1])

#테스트 횟수t만큼 숫자를 받는다.		
for i in range(t):
    k = int(input())
    pado(k)
