def solution(n, lost, reserve):
	# s = 두 집합의 교집합 체육복을 잃어버렸는데 여분의 체육복도 있는 학생
	s = set(lost) & set(reserve)
	# l = 체육복을 잃어버린 학생 중에 여분이 있는 학생을 빼서 체육복을 빌려야만 하는 학생들
	l = set(lost) - s
	# r = 여분의 체육복은 가져왔는데 도난은 안 당한 학생 (체육복을 빌려줄 수 있는 학생)
	r = set(reserve) - s
	for x in sorted(r):
		if x - 1 in l:
			l.remove(x - 1)
		elif x + 1 in l:
			l.remove(x + 1)
	return n - len(l)