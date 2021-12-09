s=input()
res=0
for x in s:
	if x.isdecimal():
		#x.isdigit() << x 가 숫자인지 판별해줌 // x.isdecimal() << 0~9까지만
		res=res*10 + int(x)
print(res)

#약수의 갯수 구하는 방법
cnt = 0
for i in range(1, res+1):
	if res%i==0:
		cnt+=1
print(cnt)
