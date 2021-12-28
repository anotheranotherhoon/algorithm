def solution(tickets):
	routes = {}
	for t in tickets:
		#dictionary 와 get을 알아보자
		routes[t[0]] = routes.get(t[0], []) + [t[1]]
	for r in routes:
		routes[r].sort(reverse=True)
	stack = ["ICN"]
	path = []
	while stack:
		top = stack[-1]
		if top not in routes or len(routes[top]) == 0:
			path.append(stack.pop())
		else:
			stack.append(routes[top][-1])
			routes[top] = routes[top][:-1]
	return path[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))