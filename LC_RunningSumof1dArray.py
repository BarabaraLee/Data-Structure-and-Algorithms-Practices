class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        :time complexity: O(n)
        :space complexity: O(1)
        """
        
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
            
        return nums