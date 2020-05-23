class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        :time complexity: O(n)
        :space complexity: O(n)
        """

        return list(set(range(1,len(nums)+1)) - set(nums))