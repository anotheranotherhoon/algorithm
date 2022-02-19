sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    n = len(sizes)
    bo = []
    so = []
    for i in range(n):
        if sizes[i][0]>=sizes[i][1]:
            bo.append(sizes[i][0])
            so.append(sizes[i][1])
        else:
            bo.append(sizes[i][1])
            so.append(sizes[i][0])
    return max(bo) * max(so)

solution(sizes)