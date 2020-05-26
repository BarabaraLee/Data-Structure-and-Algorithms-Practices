class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(1)
        """
        
        n = len(nums)
        
        if not n: 
            return 0 
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        
        maxval_prev2 = nums[0]
        maxval_prev1 = max(nums[0], nums[1])

        for i in range(2, n):
            maxval_prev2, maxval_prev1 =\
            maxval_prev1, max(maxval_prev2 + nums[i], maxval_prev1)

        return maxval_prev1
    
# 1, 2, 3, 1
# 1
#    2
#       4
#          4