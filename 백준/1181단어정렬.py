import sys
input = sys.stdin.readline

n = int(input())
data = [input().strip() for _ in range(n)]
set_data = set(data)
data = list(set_data)
data.sort()
data.sort(key=len)
for i in data:
    print(i)