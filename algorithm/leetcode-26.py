class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ticks = 1
        last_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == last_num:
                continue
            else:
                nums[ticks] = nums[i]
                last_num = nums[i]
                ticks = ticks + 1
        return ticks
