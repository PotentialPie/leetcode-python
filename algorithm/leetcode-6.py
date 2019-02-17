class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or numRows >= len(s):
            return s

        n = numRows
        z = [''] * n
        rn = list(range(0, n - 1)) + list(range(n - 1, 0, -1))  # row number for each loop. the size is 2n-2
        print(rn)
        s_len = len(s)
        i = 0  # character number
        for l in range(s_len // (2 * n - 2) + 1):  # loop number. this will chang the column number
            for j in range(2 * n - 2):
                z[rn[j]] += s[i]
                #print(z)
                if i == (s_len - 1):
                    return "".join(z)
                else:
                    i = i + 1

solution = Solution()
print(solution.convert('PAYPALISHIRING',4))