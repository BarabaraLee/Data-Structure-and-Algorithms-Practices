class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(1)
        """
        if len(nums) <= 1:
            return len(nums)
        
        current_len = 1
        global_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_len += 1
                global_len = max(current_len, global_len)
            else:
                current_len = 1
                
        return global_len
    
