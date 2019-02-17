class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or not s.strip():
            return 0

        words = s.strip().split(" ")
        for i in range(len(words) - 1, -1, -1):
            if not words[i].strip():
                continue
            return len(words[i].strip())

solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
print(solution.lengthOfLastWord('  '))
print(solution.lengthOfLastWord(" Hello "))
print(solution.lengthOfLastWord("Hello "))
print(solution.lengthOfLastWord(" Hello"))
print(solution.lengthOfLastWord(" Hello World"))
print(solution.lengthOfLastWord("Hello World "))
print(solution.lengthOfLastWord("    Hello      World    "))