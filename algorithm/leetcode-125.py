class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # newS = ''
        #
        # for sc in s:
        #     if sc.isalnum():
        #         newS += sc
        #
        # newS = newS.lower()
        #
        # if not newS:
        #     return True
        #
        # i, j = 0, len(newS) - 1
        #
        # while i <= j:
        #     if newS[i] == newS[j]:
        #         i += 1
        #         j -= 1
        #     else:
        #         return False
        # return True
        # if not s:
        #     return True
        #
        # i, j = 0, len(s)-1
        #
        # while i <= j:
        #     if not s[i].isalnum():
        #         i = i + 1
        #     elif not s[j].isalnum():
        #         j = j - 1
        #     elif s[i].lower() != s[j].lower():
        #         return False
        #     else:
        #         i = i + 1
        #         j = j - 1
        # return True
        if not s:
            return True

            # s = s.strip()
        s = s.lower()

        i, j = 0, len(s) - 1

        while i <= j:
            if not s[i].isalnum():
                i = i + 1
            elif not s[j].isalnum():
                j = j - 1
            elif s[i] != s[j]:
                return False
            else:
                i = i + 1
                j = j - 1
        return True


solution = Solution()
print(solution.isPalindrome(''))
print(solution.isPalindrome('1'))
print(solution.isPalindrome('a'))
print(solution.isPalindrome("0P"))
print(solution.isPalindrome("aa"))
print(solution.isPalindrome("ab"))
print(solution.isPalindrome("11"))
print(solution.isPalindrome("12"))
print(solution.isPalindrome("0P1"))