# # 소수 판별 함수

# def is_prime_number(x):
#     # 2부터 (x - 1)까지의 모든 수를 확인하며
#     for i in range(2, x):
#         if x % i == 0:
#             return False #소수가 아니다
#         return True #소수다

# print(is_prime_number(4))
# print(is_prime_number(7))

# # 2. 제곱근 까지만 판별하면 된다.
# import math
# # 소수 판별 함수
# def is_prime_number(x):
#     # 2 부터 x의 제곱근 까지의 모든 수를 확인하며
#     for i in range(2, int(math.sqrt(x))+1):
#         # x가 해당 수로 나누어 떨어진다면
#         if x % i  == 0:
#             return False
#     return True
# print(is_prime_number(4))
# print(is_prime_number(7))

# # 에라토스테네스의 체
# import math
# n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
# array = [True for i in range(n+1)]
# # 에라토스테네스의 체 알고리즈
# for i in range(2, int(math.sqrt(n))+1):
#     if array[i] == True:
#         j = 2
#         while i * j <= n:
#             array[i * j] = False
#             j+=1

# for i in range(2, n+1):
#     if array[i]: #array[i] == True 라면 출력
#         print(i, end=' ')