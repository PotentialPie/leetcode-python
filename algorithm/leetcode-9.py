class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x < 0:
        #     return False
        #
        # str_x = str(x)
        #
        # is_pali = True
        #
        # i = 0
        # j = len(str_x) - 1
        # while j > i:
        #     if str_x[i] == str_x[j]:
        #         i = i + 1
        #         j = j - 1
        #     else:
        #         is_pali = False
        #         break
        #
        # return is_pali
        # one line solution
        return x >= 0 and str(x)[::-1] == str(x)

solution = Solution()
print(solution.isPalindrome('-5'))
print(solution.isPalindrome('0'))
print(solution.isPalindrome('7'))
print(solution.isPalindrome('12'))
print(solution.isPalindrome('22'))
print(solution.isPalindrome('212'))
print(solution.isPalindrome('2222'))
print(solution.isPalindrome('1221'))
print(solution.isPalindrome('12521'))
print(solution.isPalindrome('12522'))
print(solution.isPalindrome('-12522'))