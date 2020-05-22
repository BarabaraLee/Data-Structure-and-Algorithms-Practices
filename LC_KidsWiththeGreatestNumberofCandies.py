class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        :time complexity: O(n)
        :space complexity: O(1)
        """
        
        return [x + extraCandies >= max(candies)  for x in candies]