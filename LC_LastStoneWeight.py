class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(1)
        """
        from heapq import heapify, heappop, heappush
        
        stones = [-x for x in stones]
        heapify(stones)
        
        while stones and len(stones) >= 2:
            first = -heappop(stones)
            second = -heappop(stones)
            if first != second:
                heappush(stones, -(first - second))
                
        return 0 if not stones else -stones[0]