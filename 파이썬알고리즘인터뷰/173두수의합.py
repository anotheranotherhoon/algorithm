nums = [2, 7, 11, 15]
target = 9
length = len(nums)
result = []
for i in range(length):
	for j in range(1, length):
		if nums[i]+nums[j] == target:
			result.append((i,j))
print(result)

