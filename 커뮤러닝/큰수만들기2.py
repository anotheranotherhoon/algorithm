def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        # collected가 비어있지 않고 가장 끝에 있는 요소가 그 다음 숫자 보다 작고 바꿀 기회가 남아 있을 때
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -=1
        # 뺼 수 있는 기회를 다썼으면 다담는다.
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    # 만약에 k가 0보다 클경우 collected에서 끝에서 k번째 까지 자른다.
    collected = collected[:-k] if k > 0 else collected
    # 배열에 있는 숫자들을 합친다.
    answer = ''.join(collected)
    return answer


number = "4177252841"
k = 4
print(solution(number, k))