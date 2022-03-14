from collections import defaultdict
from collections import Counter
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        a1 = {'a': 999,'e':999,'i':999,'o':999,'u':999}
        a2 = defaultdict(int)
        res = 0
        for i in range(len(s)):
            if i >= k:
                a2[s[i - k]] -= 1
            a2[s[i]] += 1
            res = max(res, sum((a1 - (a2 - a1)).values()))
        return res

nums = [9,4,1,7]

s1 = "abciiidef"

s2 = "eidbaooo"


s = Solution()
print(s.maxVowels( s1,3))

