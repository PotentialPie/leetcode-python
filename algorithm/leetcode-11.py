class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        llen = len(height)
        head = 0
        tail = llen - 1
        maxarea = -1
        while head < tail:
            temp_height = min(height[head], height[tail])
            temp_width = tail - head
            temp_area = temp_height * temp_width
            if temp_area > maxarea:
                maxarea = temp_area
            if height[head] < height[tail]:
                head = head + 1
            else:
                tail = tail - 1
        return maxarea


solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print('c'*3 + 'b')