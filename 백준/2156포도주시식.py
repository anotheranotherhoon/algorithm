n = int(input())
array = [0] * 100000
for i in range(n):
    array[i]=int(input())

d=[0] * 10000
d[0] = array[0]
d[1] = array[0]+array[1]
# 자신과 두개 앞의 것, 자신과 하나 앞의 것, 자신을 포함하지 않는 경우
d[2] = max(array[2]+array[0], array[2]+array[1], d[1])
for i in range(3, n):
    #d[i-1]은 자신을 포함하지 않는 경우의 수
    d[i] = max(array[i]+d[i-2], array[i]+array[i-1]+d[i-3], d[i-1])
print(max(d))