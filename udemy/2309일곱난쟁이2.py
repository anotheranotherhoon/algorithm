data = [int(input()) for _ in range(9)]
data.sort()
tot = sum(data)
def f():
    for i in range(9):
        for j in range(i+1, 9):
            if tot-(data[i] + data[j]) == 100:
                for k in range(9):
                    if i != k and j != k:
                        print(data[k])
                return
f()