num, m = map(int,input().split())
num=list(map(int, str(num)))
stack=[]
for x in num:
	# while stack 만 적으면 비어있으면 거짓 있으면 참//스택이 비어있지 않고 m>0이고 스택에 맨 뒷 자료가 나 보다 작으면 맨 뒷 자료 팝
	while stack and m>0 and stack[-1]<x:
		stack.pop()
		m-=1
	stack.append(x)
if m!=0:
	stack=stack[:-m]
#str을 join 시킴
res=''.join(map(str, stack))
print(res)