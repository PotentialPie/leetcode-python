class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # n = len(s)
        #
        # if s[0] == '0':
        #     return 0
        #
        # dp = [0 for i in range(n)]
        # if n >= 1:
        #     dp[0] = 1
        # if n >= 2 and int(s[0:2]) <= 26 and s[1] != '0':
        #     dp[1] = 2
        # if n >= 2 and int(s[0:2]) > 26 and  s[1] != '0':
        #     dp[1] = 1
        # if n >= 2 and int(s[0:2]) > 26 and  s[1] == '0':
        #     dp[1] = 0
        # if n >= 2 and int(s[0:2]) <= 26 and  s[1] == '0':
        #     dp[1] = 1
        #
        # for i in range(2, n):
        #     if s[i] == '0' and (int(s[i - 1:i + 1]) > 26 or s[i - 1] == '0'):
        #         dp[i] = 0
        #         break
        #     if s[i] == '0' and int(s[i - 1:i + 1]) <= 26:
        #         dp[i] = dp[i - 2]
        #     if s[i] != '0' and (int(s[i - 1:i + 1]) > 26 or s[i - 1] == '0'):
        #         dp[i] = dp[i - 1]
        #     if s[i] != '0' and int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
        #         dp[i] = dp[i - 1] + dp[i - 2]
        # #print(dp)
        # return dp[n - 1]
        if s == "0":
            return 0
        w, w1, w2 = 1, 0, 0
        for c in s:
            i = int(c)
            w, w1, w2 = int(i != 0) * w + w1 + int(0 <= i <= 6) * w2, int(i == 1) * w, int(i == 2) * w
        return w

solution = Solution()
print(solution.numDecodings("0"))
print(solution.numDecodings("1"))
print(solution.numDecodings("9"))
print(solution.numDecodings("01"))
print(solution.numDecodings("12"))
print(solution.numDecodings("00"))
print(solution.numDecodings("27"))
print(solution.numDecodings("72"))
print(solution.numDecodings("123"))
print(solution.numDecodings("321"))
print(solution.numDecodings("301"))
print(solution.numDecodings("901"))
print(solution.numDecodings("109"))
print(solution.numDecodings("309"))
print(solution.numDecodings("039"))
print(solution.numDecodings("015"))
print(solution.numDecodings("190"))
