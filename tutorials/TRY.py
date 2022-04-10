class Solution:
    def numberOfWays(self, s: str) -> int:
        os = 0
        ls = 0
        res = 0
        for i in range(len(s)):
            if int(s[i]) == 1:
                ls += 1
            else:
                os += 1
        l, r = 0, len(s) - 1
        temp = os
        while l < r:
            if int(s[l]) == 0:
                l += 1
                temp -= 1
            if int(s[r]) == 0:
                r -= 1
                temp -= 1
            if int(s[l]) == int(s[r]) == 1:
                res += temp
                if int(s[l + 1]) == 1:
                    l += 1
                else:
                    r -= 1
        l, r = 0, len(s) - 1
        temp = ls
        while l < r:
            if int(s[l]) == 1:
                l += 1
                temp -= 1
            if int(s[r]) == 1:
                r -= 1
                temp -= 1
            if int(s[l]) == int(s[r]) == 0:
                res += temp
                if int(s[l + 1]) == 0:
                    l += 1
                else:
                    r -= 1
        return res

nums = "0001100100"
s = Solution()
print(s.numberOfWays(nums))
