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

# #8
# from bisect import bisect_left, bisect_right
# a = [1, 2, 4, 4, 8]
# x = 4
# print(bisect_left(a, x))
# print(bisect_right(a, x))

# #9
# from bisect import bisect_right, bisect_left

# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, right_value)
#     left_index = bisect_left(a, left_value)
#     return right_index - left_index

# a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
# print(count_by_range(a, 4, 4)) # 값이 4인 데이터 개수 출력 왼쪽에서 4의 위치와 오른쪽에서 4의 위치를 빼는 거니까
# print(count_by_range(a, -1, 3))# -1 부터 3범위에 있는 데이터 개수 출력

# #10
# from collections import Counter
# counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
# print(counter['blue'])
# print(counter['green'])
# print(counter)
# print(dict(counter))