class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        num = digits[-1] + 1
        digits[-1] = num%10
        carry = num//10
        i = len(digits)-2
        while carry != 0:
            if i < 0:
                digits.insert(0,1)
                break
            num = digits[i] + carry
            digits[i] = num%10
            carry = num//10
            i = i - 1
        return digits

solution = Solution()
print(solution.plusOne([1,2,3]))
print(solution.plusOne([4,3,2,1]))
print(solution.plusOne([4,3,2,0]))
print(solution.plusOne([4,3,9,9]))
print(solution.plusOne([4]))
print(solution.plusOne([9]))
print(solution.plusOne([9,9]))


# a = [1,2,3]
# a.insert(0,3)
# print(a)