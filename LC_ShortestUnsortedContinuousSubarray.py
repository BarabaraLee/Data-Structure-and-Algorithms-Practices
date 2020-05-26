class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :time complexity: O(n*log(n))
        :space complexity: O(n)
        """
        nums_sorted = sorted(nums)
        
        if nums == nums_sorted:
            return 0
        
        n = len(nums)

        i = 0
        while i < n and nums[i] == nums_sorted[i]:
            i += 1

        j = n - 1
        while j >=0 and nums[j] == nums_sorted[j]:
            j -= 1
            
        return j - i + 1