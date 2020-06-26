class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        :time complexity: O(n)
        :space complexity: O(1)
        """
        if not A or not A[0]:
            return A
        
        r, c = len(A), len(A[0])
        
        for i in range(r):
            left,right = 0, c-1
            while left < right:
                A[i][left], A[i][right] = A[i][right], A[i][left]
                left += 1
                right -= 1
            for j in range(c):
                A[i][j] = 1 - A[i][j]
        
        return A