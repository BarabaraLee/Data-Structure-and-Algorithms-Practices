class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        :time complexity: O(n^0.5)
        :space complexity: O(1)
        """
        from math import sqrt
        
        a = 0
        while a * a <= c:
            b = sqrt(c - a * a)
            if b == int(b):
                return True
            a += 1
            
        return False