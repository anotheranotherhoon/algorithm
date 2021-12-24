# 동적계획법(Dynamic Programming)
# 주어진 최적화 문제를 재귀적인 방식으로 보다 작은 부분 문제로 나누어 부분 문제를 풀어, 이 해를 조합하여 전체 문제의 해답에 
# 이르는 방식
# 알고리즘의 진행에 따라 탐색해야 할 범위를 동적으로 결정함으로써 탐색 범위를 한정할 수 있음
def solution(N, number):
	s = [set() for x in range(8)]
	for i, x in enumerate(s, start=1):
		x.add(int(str(N) * i))
	for i in range(1, len(s)):
		for j in range(i):
			for op1 in s[j]:
				for op2 in s[i - j - 1]:
					s[i].add(op1 + op2)
					s[i].add(op1 - op2)
					s[i].add(op1 * op2)
					if op2 !=0:
						s[i].add(op1 // op2)
		if number in s[i]:
			answer = i + 1
			break
		else:
			answer = -1
	return answer	

