class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(1)
        """
        globalmax = 0
        currentmax = 0
        
        for x in nums:
            if x == 1:
                currentmax += 1
            elif x == 0:
                globalmax = max(globalmax, currentmax)
                currentmax = 0
                
            globalmax = max(globalmax, currentmax)
                
        return globalmax 