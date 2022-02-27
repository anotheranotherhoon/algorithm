nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums,9))

def twoSum(nums, target):
    left, right = 0, len(nums)-1
    while not left == right:
        # 두 수의 합이 타겟보다 작을 경우 left의 값을 오른쪽으로 이동시킨다.
        if nums[left]+nums[right] < target:
            left +=1
        elif nums[left]+nums[right] > target:
            right +=1
        else:
            return [left, right]