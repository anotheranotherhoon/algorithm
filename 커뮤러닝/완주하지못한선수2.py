def solution(participant, completion):
    d = {}
    for x in participant:
        # 주어진 키 x가 처음 등장하면 1로 만들고 이미 존재하는 키라면 +1
        d[x] = d.get(x, 0) + 1
    for x in completion:
        d[x] -= 1
    # v가 0 보다 큰 것의 키를 담아라 .items() < 사전에 키와 밸류를 리턴한다.
    dnf = [ k for k, v in d.items() if v > 0]
    answer =dnf[0]
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
solution(participant, completion)