# def rain(data):
#     n = len(data)
#     answer = 0
#     water = 0
#     maxindex = 0
#     max = -2147000000
#     for i, v in enumerate(data):
#         if i == 0 and v ==0:
#             continue
#         elif water == 0 
#         elif v > max:
#             for j in data[maxindex:i]:
#                 water += (v-1)-j
#             answer.append(water)
#             water = 0
#             maxindex = i
#             max = v
#         elif v == max:
#             for j in data[maxindex:i]:
#                 water += v-j
#             answer.append(water)
#             water = 0
#             maxindex = i
#             max = v
            
#     return answer
# print(rain(data))

data = [0,1,0,2,1,0,1,3,2,1,2,1]

def trap(data):
    stack = []
    volume = 0
    for i in range(len(data)):
        # 변곡점을 만나는 경우
        while stack and data[i] > data[stack[-1]]:
            top = stack.pop()
            if not len(stack):
                break
            distance = i - stack[-1] - 1
            waters = min(data[i], data[stack[-1]]) - data[top]
            volume += distance * waters
        stack.append(i)
    return volume

print(trap(data))