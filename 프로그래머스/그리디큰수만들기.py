# 큰 수 만들기 - 원칙
# 앞 자리에 큰 수가 오는 것이 전체를 크게 만든다.
# 따라서, 큰 것을 우선해서 골라 담고 싶다.
# 큰 수 만들기 - 방법
# 앞 자리에서부터 하나씩 골라서 담되,
# 지금 담으려는 것보다 작은 것들은 도로 뺀다!
# 단, 뺄 수 있는 수효에 도달할 때 까지만
# 큰 수가 앞자리에, 작은 수가 뒷 자리에 놓이도록
def solution(number, k):
	collected = []
	for i, num in enumerate(number):
		while len(collected) > 0 and collected[-1] < num and k > 0:
			collected.pop()
			k -= 1
		if k == 0:
			collected += list(number[i:])
			break
		collected.append(num)
	collected=collected[:-k] if k > 0 else collected
	answer = ''.join(collected)
	return answer