class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ticks = 0
        if not nums:
            return 0
        for nums_index in range(len(nums)):
            if nums[nums_index] == val:
                continue
            else:
                nums[ticks] = nums[nums_index]
                ticks = ticks + 1
        return ticks