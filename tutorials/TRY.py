# import bisect
# class Solution:
#     def halveArray(self, nums) -> int:
#         target = sum(nums) / 2
#         aaa = sum(nums)
#         res = 0
#         nums.sort()
#         nums = nums[::-1]
#         while aaa > target:
#             aaa -= nums[-1] / 2
#             res += 1
#             nums[-1] /= 2
#             temp = nums[-1]
#             weizhi = bisect.bisect_left(nums, temp)
#             if weizhi != len(nums) - 1:
#                 nums.pop()
#                 nums = nums[:weizhi] + [temp] + nums[weizhi:]
#
#         return res
#
# S = Solution()
# text = [6,58,10,84,35,8,22,64,1,78,86,71,77]
#
# pattern = "ac"
# print(S.halveArray(text))
i = 1
sum = 2
while sum < 10000000:
    sum *= 2
    i += 1
print(i)