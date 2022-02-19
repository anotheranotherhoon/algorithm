def solution(participant, completion):
    player = list(set(participant)-set(completion))
    if player:
        return player[0]   


participant = ["mislav", "kyle"]
completion = ["kyle"]

solution(participant, completion)