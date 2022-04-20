# 4 5 2 0 6 3 -56 3 -1

nums = list(map(int, input().split()))
for j in range(len(nums)):

    for i in range(len(nums)-1-j):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

print(nums)
