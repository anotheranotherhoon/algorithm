# data =[]
# for i in range(11):
#     data.append(i)
# data.insert(0,11)
# print(data)

def twoSum(nums, target):
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement)+(i+1)]

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums,9))