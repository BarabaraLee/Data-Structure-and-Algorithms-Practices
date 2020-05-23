class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        :time complexity: O(n)
        :space complexity: O(1)
        """
        maxavg = 1. * sum(nums[:k]) / k
        lastavg = maxavg
        for i in range(1 , len(nums) - k + 1):
            # remove the i-1, add i + k - 1
            curavg = 1. * (lastavg * k - nums[i - 1] + nums[i + k - 1]) / k
            maxavg = max(maxavg, curavg)
            lastavg = curavg
            
        return maxavg
    
# i -> i + k - 1    
# 1 -> k
# 2 -> k+1
# ...
# n-k -> n-1