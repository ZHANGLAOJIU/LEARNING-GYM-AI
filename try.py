def minimalKSum(nums, k):
    nums.append(0)
    nums = list(set(nums))
    nums.sort()
    res = 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] - 1 < k:
            res += int((nums[i] + nums[i - 1]) * (nums[i] - nums[i - 1] - 1) / 2)
            k -= nums[i] - nums[i - 1] - 1
        else:
            res += int((2 * nums[i - 1] + 1 + k) * k / 2)
            return int(res)
    res += int((2 * nums[-1] + 1 + k) * k / 2)
    return int(res)

nums = [1000000000]


print(minimalKSum(nums, 1000000000))