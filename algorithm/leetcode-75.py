class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        s_index = 0
        e_index = n - 1
        tmp = nums[0]
        i = 0
        while i <= e_index:
            if nums[i] == 0:
                tmp = nums[s_index]
                nums[s_index] = 0
                nums[i] = tmp
                s_index = s_index + 1
                i = i + 1
            elif nums[i] == 2:
                tmp = nums[e_index]
                nums[e_index] = 2
                nums[i] = tmp
                e_index = e_index - 1
            else:
                i = i + 1
            print(nums)

solution = Solution()
print(solution.sortColors([2,0,2,1,1,0]))
print(solution.sortColors([0,2,1,1,1,0]))
print(solution.sortColors([2,1,0]))
print(solution.sortColors([2,1,0,0,0]))
print(solution.sortColors([0,1,2,0,1,2,2,0,1,2,1,0,0,0]))
