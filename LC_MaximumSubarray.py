class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(1)
        """
        import sys
        globalmax = nums[0]
        localmax = nums[0]
        
        for i in range(1,len(nums)):
            localmax = max(nums[i], localmax + nums[i])
            globalmax = max(globalmax, localmax)
                
        return globalmax
                
                
#           [-2, 1,-3, 4,-1]       
                           
# globalmax  -   1  1  4  4
# localmax  -2   1 -2  4  3