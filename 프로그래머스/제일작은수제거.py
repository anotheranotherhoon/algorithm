# def solution(arr):
#     answer = []
#     min = int(1e9)
#     minindex = 0
#     for i in range(len(arr)):
#         if arr[i] == 10:
#             min = 10
#         elif arr[i] < min:
#             minindex = i
#             min = arr[i]
#     if min != 10:
#         arr.pop(minindex)
#         answer=arr
#     else:
#         answer.append(-1)
#     return answer
# 틀렸다.