class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s.remove(num)
                
        
        return s.pop()