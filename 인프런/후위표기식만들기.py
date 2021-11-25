a=input()
stack=[]
res=''
for x in a:
	#.isdecimal() 숫자인지 확인해준다
	if x.isdecimal():
		res+=x
	else:
		if x=='(':
			stack.append(x)
		elif x=='*' or x=='/':
			while stack and (stack[-1]=='*' or stack[-1]=="/"):
				res+=stack.pop()
			stack.append(x)
		elif x=='+' or x=='-':
			while stack and stack[-1]!='(':
				res+=stack.pop()
			stack.append(x)
		elif x==')':
			while stack and stack[-1]!='(':
				res+=stack.pop()
			stack.pop()
while stack:
	res+=stack.pop()
print(res)