def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [4, 1, 2, 1, 2]
### result에 차곡 차곡 더해지다가 같은 숫자를 만나면 사라진다.
print(singleNumber(nums))