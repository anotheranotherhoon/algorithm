n = int(input())
nth = 666
count = 0

while True:
    if '666' in str(nth):
        count += 1
    if count == n:
        print(nth)
        break
    nth += 1

# 1666 두 번째는 2666 앞에 숫자를 붙일 생각을 했었다. 하지만 정답은 666부터 숫자를 하나 씩 늘려갔어야 했다.