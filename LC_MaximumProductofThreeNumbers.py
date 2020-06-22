class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
            
        max1, max2, max3 = -sys.maxsize, -sys.maxsize, -sys.maxsize
        min1, min2 = sys.maxsize, sys.maxsize
        
        for x in nums:
            if x > max1:
                max1, max2, max3 = x, max1, max2
                
            elif x< max1 and x > max2:
                max2, max3 = x, max2
                
            elif x< max2 and x > max3:
                max3 = x
                
            if x < min1:
                min1, min2 = x, min1
            elif x > min1 and x < min2:
                min2 = x
                    
        return max(max1*max2*max3, max1*min1*min2)