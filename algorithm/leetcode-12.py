#coding=utf-8
# 这题能告诉我们什么呢？
# 学到的是，字典的key，如果遍历的话，排序是按字段顺
class Solution:
    trans_dict = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
    key_list = [1000, 500, 100, 50, 10, 5, 1]
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #print(num)
        if num == 0:
            return ''
        # if num >= 1000:
        #     times = num//1000
        #     return 'M'*times + self.intToRoman(num - 1000*times)
        if num >= 900 and num < 1000:
            return 'CM'+ self.intToRoman(num - 900)
        if num >= 400 and num < 500:
            return 'CD' + self.intToRoman(num - 400)
        if num >= 90 and num < 100:
            return 'XC'+ self.intToRoman(num - 90)
        if num >= 40 and num < 50:
            return 'XL' + self.intToRoman(num - 40)
        if num >= 9 and num < 10:
            return 'IX'+ self.intToRoman(num - 9)
        if num >= 4 and num < 5:
            return 'IV' + self.intToRoman(num - 4)
        for key in self.key_list:
            if num >= key:
                times = num // key
                return self.trans_dict[key] * times + self.intToRoman(num - key * times)

solution = Solution()
print(solution.intToRoman(1))
print(solution.intToRoman(4))
print(solution.intToRoman(19))
print(solution.intToRoman(49))
print(solution.intToRoman(99))
print(solution.intToRoman(399))
print(solution.intToRoman(3399))
print(solution.intToRoman(3499))
print(solution.intToRoman(3999))

trans_dict = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
for key in trans_dict:
    print(key)