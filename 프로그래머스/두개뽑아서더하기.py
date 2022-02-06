def solution(numbers):
    length = len(numbers)
    answer = set()
    for i in range(length-1):
        for j in range(i+1,length):
            result = numbers[i] + numbers[j]
            answer.add(result)
    result = list(answer)
    result.sort()
    return result