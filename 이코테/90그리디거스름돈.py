n=1260
count=0

coin_types=[500, 100, 50, 10]

for coin in coin_types:
	count += n //coin # 1260을 동전으로 나눈 몫 만큼 더함
	n=n%coin
print(count)

# 단위가 서로 배수 형태가 아니라, 무작위로 주어진 경우에는 그리디 알고리즘으로는 해결할 수 없다.