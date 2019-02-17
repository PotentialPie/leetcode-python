class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a) - 1
        n = len(b) - 1

        result = ''
        carry = 0

        while True:
            if m >= 0 and n >= 0:
                condition = int(a[m]) + int(b[n]) + carry
            elif m >= 0 and n < 0:
                condition = int(a[m]) + carry
            elif m < 0 and n >= 0:
                condition = int(b[n]) + carry
            else:
                if carry == 1:
                    result = '1'+result
                break
            if condition == 3:
                result = '1'+result
                carry = 1
            elif condition == 2:
                result = '0'+result
                carry = 1
            elif condition == 1:
                result = '1'+result
                carry = 0
            else:
                result = '0'+result
                carry = 0
            m = m - 1
            n = n - 1
        return result


solution = Solution()
print(solution.addBinary(a = "11", b = "1"))
print(solution.addBinary(a = "1010", b = "1011"))
print(solution.addBinary(a = "0", b = "0"))
print(solution.addBinary(a = "1", b = "0"))
print(solution.addBinary(a = "1", b = "1"))
print(solution.addBinary(a = "01", b = "10"))

