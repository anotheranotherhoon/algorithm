n=int(input())
#딕셔너리를 선언
p=dict()
for i in range(n):
	word=input()
	p[word]=1
for i in range(n-1):
	word=input()
	p[word]=0
# .items() key, value 쌍을 얻는다
for key, val in p.items():
	if val==1:
		print(key)
		break