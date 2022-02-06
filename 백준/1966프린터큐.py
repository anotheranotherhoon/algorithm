from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    data = deque([map(int, input().split())])
    cnt = 0
    while data:
        max = max(data)
        q = data.popleft()
        cnt = 1
        m -= 1
        if q == max:
            cnt += 1
            if m < 0:
                print(cnt)
                break
            
            else:
                data.append(q)
                if m<0:
                    m = len(data)-1
            

