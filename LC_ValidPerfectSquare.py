class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        :time complexity: O(log(n))
        :space complexity: O(1)
        """
        start, end = 1, num 
        
        while start <= end:
            mid = start + (end - start) // 2
            if num < mid ** 2:
                end = mid - 1
            elif num > mid ** 2:
                start = mid + 1
            else:
                return True
            
        return False