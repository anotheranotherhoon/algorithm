from itertools import combinations

# 값을 입력받아 치킨집과 집을 구분하여 리스트에 저장한다.
N, M = map(int, input().split())
houses = []
chickens = []
for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            chickens.append((i, j))

# 치킨집과 집과의 거리를 계산한다.
def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 좌우상단과 우좌하단사이의 거리가 최대 거리이다.
ans = 2 * N * len(houses)

# 치킨집의 조합중에서 M개 만큼을 선택
for combi in combinations(chickens, M):
    tot = 0 #도시의 치킨거리
    for house in houses:
            tot += min(get_dist(house, chicken) for chicken in combi)
    ans = min(ans, tot)

print(ans)