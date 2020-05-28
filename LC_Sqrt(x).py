class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        :time complexity: O(log(n))
        :space complexity: O(1)
        """
        start, end = 0, x
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if mid ** 2 > x:
                end = mid - 1
            elif mid ** 2 < x:
                start = mid + 1
            else:
                return mid
        
        return min(start, end)