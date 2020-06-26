class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        :time complexity: O(r*c)
        :space complexity: O(r*c)
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        
        oneD = []
        
        for num_list in nums:
            oneD += num_list
            
        res = []
        for i in range(r):
            res.append(oneD[i*c : i*c +c])
            
        return res