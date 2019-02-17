#coding=utf-8
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        print(-int(2**31))
        #if x >= 2e31 or x < -2e31 or x == 0:
        # 注意，2e31和2**31的区别
        if x >= 2**31 or x <= -2**31 or x == 0:
            return 0
        str_x = str(x)
        # [i:j:s]的意思是，从i到j，步长为s
        # 如果s<0，则i，j都为负数，从倒数开始算
        # 例如s[-1:-len(s)-1:-1]就代表反转
        if x < 0:
            result = int('-'+str(int(str_x[-1:-len(str_x):-1])))
            # 千万别忘了，反转的记过也要判断啊！！！！！！
            if result >= 2 ** 31 or result <= -2 ** 31 or result == 0:
                return 0
            return result
        else:
            result = int(str(int(str_x[-1:-len(str_x)-1:-1])))
            if result >= 2 ** 31 or result <= -2 ** 31 or result == 0:
                return 0
            return result

solution = Solution()
print(solution.reverse(4236469))