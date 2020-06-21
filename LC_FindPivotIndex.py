class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(n)
        """
        if not nums:
            return -1
        
        sumcum = []
        sumcum.append(nums[0])
        
        n = len(nums)
        
        for i in range(1, n):
            sumcum.append(nums[i] + sumcum[i-1]) 
            
        for i in range(n):
            
            if i == 0:
                leftsum = 0
            else:
                leftsum = sumcum[i - 1]
                
            if i == len(nums) - 1:
                rightsum = 0
            else: 
                rightsum = sumcum[n - 1] - nums[i] - sumcum[i-1]
                
            if leftsum == rightsum:
                return i
        return -1
                
                
        