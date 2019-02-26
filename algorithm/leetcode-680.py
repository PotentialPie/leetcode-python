class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def check(s, flag):
            if not s:
                return True
            if s[0] == s[-1]:
                return check(s[1:len(s) - 1], flag)
            else:
                if flag:
                    return check(s[1:], False) or check(s[:len(s) - 1], False)
                else:
                    return False

        return check(s, True)

solution = Solution()
print(solution.validPalindrome(''))
print(solution.validPalindrome('a'))
print(solution.validPalindrome('ab'))
print(solution.validPalindrome('aa'))
print(solution.validPalindrome('aba'))
print(solution.validPalindrome('aaa'))
print(solution.validPalindrome('aab'))
print(solution.validPalindrome('abc'))
print(solution.validPalindrome('abca'))