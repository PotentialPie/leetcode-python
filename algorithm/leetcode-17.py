#coding=utf-8
class Solution:
    result_list = []
    # 1的特殊情况如果想处理的话，一定要好好处理啊！
    num2letters_dict = {'1': [''],
                        '2': ['a', 'b', 'c'],
                        '3': ['d', 'e', 'f'],
                        '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'],
                        '6': ['m', 'n', 'o'],
                        '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'],
                        '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ## 边界！边界！边界！ 说了多少次，输入的边界一定要考虑空空！空空！空空！
        if not digits:
            return []
        self.result_list = []
        self.dfs(digits, '')
        return self.result_list

    def dfs(self, left_digits, temp_str):
        #print(left_digits, temp_str)
        if not left_digits:
            #print(1)
            self.result_list.append(temp_str)
        else:
            for letter in self.num2letters_dict[left_digits[0]]:
                self.dfs(left_digits[1:], temp_str + letter)

solution = Solution()
print(solution.letterCombinations('23'))
print(solution.letterCombinations('323'))