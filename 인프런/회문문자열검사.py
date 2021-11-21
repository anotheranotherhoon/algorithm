# n = int(input())
# for i in range(n):
# 	s=input()
# 	s=s.upper()
# 	size=len(s)
# 	for j in range(size//2):
# 		if s[j] != s[-1-j]:
# 			print("#%d NO" %(i+1))
# 			break
# 	else:
# 		print("#%d YES" %(i+1))

n=int(input())
for i in range(n):
	s=input()
	s=s.upper()
	if s==s[::-1]:
		print("#%d YES" %(i+1))
	else:
		print("#%d NO" %(i+1))


# %d 정수(integer) %f 실수(float) %s 문자열(string라
# s[::-1] 문자열을 거꾸로 바꿔라 슬라이스 한 방법