class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(1)
        """
        
        if len(prices) <= 1:
            return 0
        
        import sys

        up2nowmin = sys.maxsize
        globalbest = -sys.maxsize

        for i in range(len(prices) - 1):
            up2nowmin = min(prices[i], up2nowmin)
            globalbest = max(prices[i + 1] - up2nowmin, globalbest)

        return max(globalbest, 0)