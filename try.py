from collections import defaultdict
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = defaultdict(int)
        a0 = Counter(s1)
        for i in range(len(s2)):
            if i >= len(s1):
                a[s2[i - len(s1)]] -= 1
            a[s2[i]] += 1
            if a == a0:
                return True
        return False

nums = [9,4,1,7]

s1= "ab"
s2 = "eidbaooo"


s = Solution()
print(s.checkInclusion( s1,s2))

