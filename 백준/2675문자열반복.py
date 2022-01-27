T = int(input())
for _ in range(T):
    num, word = input().split()
    for i in word:
        print(i*int(num), end='')
    print()