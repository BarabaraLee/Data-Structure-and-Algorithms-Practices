class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        from heapq import heapify, heappush, heappop
        
        self.k = k
        self.nums = nums
        heapify(self.nums) 
        
        while len(self.nums) > k:
            heappop(self.nums)
            
    def add(self, val):
        """
        :type val: int
        :rtype: int
        :time complexity: O(1)
        :space complexity: O(1)
        """
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        else:
            heappushpop(self.nums, val)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)