# #1
# score = 85
# result = "Success" if score >= 80 else "Fail"
# print(result)

# #2
# a = [1, 2, 3, 4, 5, 5, 5]
# remove_set = {3, 5}
# result = { i for i in a if i not in remove_set}
# print(result)

# #3
# a = 0

# def func():
#     global a
#     a += 1

# for i in range(10):
#     func()
    
# func()를 10번 호출해서 a가 10번 1만큼 커져서 10을 출력한다.
# print(a)

# #4
# def add(a, b):
#     return a+b
# print(add(3, 7))
# print((lambda a, b : a + b)(3, 7))

# #5 리스트에서 3개를 뽑아 나열하는 모든 경우의 수 구하기 순열
# from itertools import permutations
# data = ['A', 'B', 'C']
# result = list(permutations(data,3))
# print(result)

# #6 데이터 순서를 고려하지 않는 조합을 구하는 방법
# from itertools import combinations
# data = ['A', 'B', 'C']
# result = list(combinations(data, 2))
# print(result)

# #7 순열
# from itertools import product
# data = ['A', 'B', 'C']
# result = list(product(data, repeat=2))
# print(result)


