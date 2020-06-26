class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        :time complexity: O(n)
        :space complexity: O(n)
        """
        from collections import Counter
        
        cntr = Counter(nums)
        
        dup = -1
        for k, v in cntr.items():
            if v == 2:
                dup = k
                break
        
        normal_sum = sum(range(1, len(nums) + 1))
        new_sum = sum(nums) - dup
        
        return [dup, normal_sum - new_sum]