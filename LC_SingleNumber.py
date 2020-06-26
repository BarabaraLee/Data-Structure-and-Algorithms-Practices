class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(n)
        """
        s = set()
        
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s.remove(num)
                
        
        return s.pop()