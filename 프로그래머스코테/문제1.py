def solution(k, m, names, amounts):
    answer = 0
    n = len(names)
    last = [0]
    cnt = 1
    uppernames = []
    for i in range(n):
        uppernames.append(names[i].upper())

    for i in range(n):
        if last[-1] == uppernames[i]:
            cnt+=1
            if cnt >= k:
                answer+=1
                last.append(uppernames[i])
                continue
        else:
            cnt =1
        if amounts[i] >= m:
            answer+=1
        last.append(uppernames[i])
    return answer

k = 3
m = 50000
names = ["msLEE", "jsKim", "jsKIM", "jskiM", "jskim", "John", "john", "John", "msLEE", "msLEE", "jsKIM", "roy"]
amounts = [950, 52524, 1400, 6055, 10000, 4512, 512, 52000, 9000, 49000, 1400, 50000]

print(solution(k, m, names, amounts))
