class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        :time complexity: O(n*log(n))
        :space complexity: O(1)
        """
        from heapq import heappop, heapify
        
        nums = [-x for x in nums]
        heapify(nums)
        
        for i in range(k):
            res = heappop(nums)
            
        return -res