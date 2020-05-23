class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        :time complexity: O(n)
        :space complexity: O(n)
        """
            
        return True if len(set(nums)) < len(nums) else False