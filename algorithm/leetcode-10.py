class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        index_s = 0
        index_p = 0
        while index_s < len(s):
            if index_p >= len(p):
                return False
            if s[index_s] == p[index_p] or p[index_p] == '.':
                index_s = index_s + 1
                index_p = index_p + 1
            elif p[index_p] == '*':
                if s[index_s] == p[index_p-1] or p[index_p-1] == '.':
                    index_s = index_s + 1
                else:
                    index_p = index_p + 1
            else:
                index_p = index_p + 1
        while index_p < len(p):
            if p[index_p] == '*':
                index_p = index_p + 1
            elif index_p < len(p) - 1 and p[index_p+1] == '*':
                index_p = index_p + 2
            else:
                return False
        return True

solution = Solution()
print('ab', '.*', solution.isMatch('ab', '.*'))
print('aab', 'c*a*b', solution.isMatch('aab', 'c*a*b'))
print('aa', 'a*', solution.isMatch('aa', 'a*'))
print('mississippi', 'mis*is*p*.', solution.isMatch('mississippi', 'mis*is*p*.'))
print('aa', 'a', solution.isMatch('aa', 'a'))
print('abcdef', 'ab.*a', solution.isMatch('abcdef', 'ab.*a'))
print('abcdef', 'ab.*.', solution.isMatch('abcdef', 'ab.*.'))
print('aa', '.*', solution.isMatch('aa', '.*'))
print('a', '.*', solution.isMatch('a', '.*'))
print('abcde', 'ab.*.*', solution.isMatch('abcde', 'ab.*.*'))
print('', '.*', solution.isMatch('', '.*'))
print('', '.', solution.isMatch('', '.'))
print('', 'a*', solution.isMatch('', 'a*'))
print('', '.a*', solution.isMatch('', '.a*'))
print('aaa', 'a*a', solution.isMatch('aaa', 'a*a'))