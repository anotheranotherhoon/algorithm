n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

#k가 3이라면 fffs << 위 순서대로 반복 될 것이기 때문에 k+1로 나눈다.
count = int(m / (k+1))
count += m %(k+1)

result = 0
result += (count) * first #가장 큰 수 더하기
result += (m-count) * second # 두 번째로 큰 수 더하기

print(result)