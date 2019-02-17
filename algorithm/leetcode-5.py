class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 1
        max_i = 0
        max_j = 0
        len_s = len(s)
        # that wrong!!
        # dp_c = [[0] * len_s] * len_s
        dp_c = [[0 for i in range(len_s)] for i in range(len_s)]
        #print(dp_c)
        for i in range(len_s):
            dp_c[i][i] = 1
            #print(dp_c)
            if i < len_s - 1 and s[i] == s[i + 1]:
                #print(i)
                dp_c[i][i + 1] = 1
                max_len = 2
                max_i = i
                max_j = i + 1
        #print(dp_c)
        for i in range(3, len_s + 1):
            for j in range(0, len_s - i + 1):
                if s[j] == s[j + i - 1]:
                    #print(i, j)
                    dp_c[j][j + i - 1] = dp_c[j + 1][j + i - 2]
                    #print(dp_c[j + 1][j + i - 2])
                    if dp_c[j][j + i - 1] != 0:
                        max_len = i
                        max_i = j
                        max_j = j + i - 1
                        print(max_i,max_j)
        return s[max_i:max_j + 1]


solution = Solution()
print(solution.longestPalindrome('abcda'))

# TODO
# Manacher Algorithm