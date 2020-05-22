class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        :time complexity: O(n)
        :space complexity: O(1)
        """
        l = len(flowerbed)
        count = 0
        
        for i in range(l):
            
            if (flowerbed[i] == 0) and (i == 0 or flowerbed[i - 1] == 0)\
            and (i == l - 1 or flowerbed[i + 1] == 0):
                count += 1
                flowerbed[i] = 1
                
            if count >= n:
                return True
            
        return False