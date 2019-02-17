#coding=utf-8
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        stack = []
        com_dict = {'(':')', '[':']', '{':'}'}
        head_index = -1
        for str_index in range(len(s)):
            # 这种问题，千万别搞错了，不是==，是看匹不匹配，所以上一个必须有限制，并且用字典来确认
            if not stack or stack[head_index] not in ['(', '[', '{'] or com_dict[stack[head_index]] != s[str_index]:
                #print(str_index)
                # 如果想不用pop的话，这里不应该用append，应该是stack[index+1] = value
                # 但是要提前定义数组长度，所以，还是pop好！！！
                stack.append(s[str_index])
                head_index = head_index + 1
                #print(stack, head_index)
            else:
                #print(str_index)
                # 要把元素删除掉啊,pop默认是删除最后一个元素
                stack.pop()
                head_index = head_index - 1
        if head_index == -1:
            return True
        else:
            return False

solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("([)]"))