class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :time complexity: O(n)
        :space complexity: O(n)
        """
        self.nums = nums
        self.dic = {0: self.nums[0]} if nums else {}
        
        for i in range(1, len(self.nums) ):
            self.dic[i] = self.dic[i - 1] + self.nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.dic[j]
        
        return self.dic[j] - self.dic[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)