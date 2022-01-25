t = int(input())
# 한번에 여러번의 테스트케이스를 처리 할 때
for _ in range(t):
    ps = list(input())
    stack = []
    is_empty = False
    for i in range(len(ps)):
        if ps[i] == '(':
            stack.append(ps[i])
        else:
            # stack이 비어있다면
            if not stack:
                is_empty = True
                break
            else:
                stack.pop()
    #스택이 비어있고 is_empty가 초기 값(False)이면
    if not stack and not is_empty:
        print('YES')
    else:
        print('NO')