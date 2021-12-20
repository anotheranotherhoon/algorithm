# n=int(input())
# data = list(map(int, input().split()))
# res = 0
# list =[]
# for i in data:
# 	res +=i
# res = res//n

# for i in data:
# 	list.append(abs(i-res))

# result = min(list)
# print(list.index(result)+1)
# 평균과 가장 가까운 점수가 여러 개 일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다. << 위의 조건에 맞지 않음


n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
min = 2147000000

for idx, x in enumerate(a):
	tmp = abs(x-ave)
	if tmp<min:
		min=tmp
		score=x
		res=idx+1
	elif tmp==min:
		if x>score:
			score=x
			res=idx+1
print(ave, res)