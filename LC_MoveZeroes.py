class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        :time complexity: O(n)
        :space complexity: O(1)
        """
        i = 0
        cnt = 0
        while i < len(nums):
            if nums[i] == 0:
                cnt += 1
                nums.pop(i)
                i -= 1
            i += 1
            
        for i in range(cnt):
            nums.append(0)
            
        return nums