from bisect import bisect_left, bisect_right
n=int(input())
data1 = sorted(list(map(int, input().split())))
m=int(input())
data2 = list(map(int, input().split()))
ans = []
for q in data2:
    # l = bisect_left(data1, q)
    # if cards[l] == q:
    l = bisect_left(data1, q)
    r = bisect_right(data1, q)
    # 만약에 같은 수가 존재 한다면 1보다 큰 수가 나올 것이고 같은 수가 없으면 r과 l이 같은 수가 나와서 0이 될것이다.
    ans.append(1 if r - l > 0 else 0)

print(' '.join(map(str, ans)))