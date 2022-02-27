# def solution(people, tshirts):
#     p = {}
#     count = 0
#     for x in people:
#         p[x] = p.get(x, 0) +1
    
#     for k, v in p.items():
#         for i in tshirts:
#             if k == i and v > 0:
#                 v-=1
#                 count += 1
#     answer = count
#     return answer

people = [2,3]
tshirts = [1,2,3]

def solution(people, tshirts):
    t = {}
    count = 0
    for x in tshirts:
        t[x] = t.get(x, 0) +1
    
    for x in people:
        if t[x]:
            t[x] -=1
            count +=1
    answer = count
    return answer

print(solution(people,tshirts))