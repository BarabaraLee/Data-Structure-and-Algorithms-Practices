class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        :time complexity: O(n)
        :space complexity: O(1)
        """
        
        n = len(A)
        
        if A[0] == A[-1]:
            for i in range(1, n):
                if A[i - 1] != A[i]:
                    return False
                
        elif A[0] > A[-1]:
            for i in range(1, n):
                if A[i - 1] < A[i]:
                    return False
                
        elif A[0] < A[-1]:
            for i in range(1, n):
                if A[i - 1] > A[i]:
                    return False