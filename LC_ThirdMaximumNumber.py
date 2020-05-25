class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(1)
        """
        import sys
        
        maxx_lst = []
        for i in range(3):
            maxx = max(nums)
            nums = [-sys.maxsize if x == maxx else x for x in nums]
            if maxx != -sys.maxsize:
                maxx_lst.append(maxx)
            
        return min(maxx_lst) if len(maxx_lst) == 3 else max(maxx_lst)