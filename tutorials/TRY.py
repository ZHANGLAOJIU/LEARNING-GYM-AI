class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows):
        dp = [0] * 12
        dic = {}
        res = [0] * 12
        for i in range(12):
            dp[i] = i / (aliceArrows[i] + 1)
            dic[dp[i]] = i, aliceArrows[i] + 1
        dp.sort()
        dp = dp[::-1]
        for i in range(12):
            if numArrows >= dic[dp[i]][1]:
                res[dic[dp[i]][0]] = dic[dp[i]][1]
                numArrows -= dic[dp[i]][1] + 1
        return res, dp, dic

S = Solution()
text = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
numArrows = 9
print(S.maximumBobPoints( numArrows,aliceArrows))
