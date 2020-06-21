class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(1)
        """
        S = sum(nums)
        leftsum = 0
        
        for i, x in enumerate(nums):
            if leftsum == S - x - leftsum:
                return i
            
            leftsum += x
        
        return -1