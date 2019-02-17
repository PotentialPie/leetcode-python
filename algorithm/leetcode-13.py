class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        trans_dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        slen = len(s)
        s_index = 0
        value = 0
        while s_index < len(s):
            if s_index == len(s) - 1:
                value = value + trans_dict[s[s_index]]
                s_index = s_index + 1
            elif trans_dict[s[s_index]] >= trans_dict[s[s_index+1]]:
                value = value + trans_dict[s[s_index]]
                s_index = s_index + 1
            else:
                value = value + trans_dict[s[s_index+1]] - trans_dict[s[s_index]]
                s_index = s_index + 2
        return value

solution = Solution()
print(solution.romanToInt("III"))
print(solution.romanToInt("IV"))
print(solution.romanToInt("IX"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))