class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur_index = 1
        cur_sequence = '1'
        if n == 1:
            return '1'
        while cur_index < n:
            tmp = ''
            i = 0
            while i < len(cur_sequence):
                cur_count = 1
                while i < len(cur_sequence) - 1 and cur_sequence[i] == cur_sequence[i+1]:
                    i += 1
                    cur_count += 1
                tmp = tmp + str(cur_count) + str(cur_sequence[i])
                i = i + 1
            if cur_index == n - 1:
                return tmp
            else:
                cur_index = cur_index + 1
                cur_sequence = tmp
                tmp = ''

solution = Solution()
print(solution.countAndSay(1))
print(solution.countAndSay(2))
print(solution.countAndSay(3))
print(solution.countAndSay(4))
print(solution.countAndSay(5))
print(solution.countAndSay(6))

a = [1]
c = []
c.append()
print(c)
a.remove(1)
print(c)