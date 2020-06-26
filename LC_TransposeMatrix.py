class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        :time complexity: O(n*n)
        :space complexity: O(1)
        """
        n, m = len(A), len(A[0])
        
        B = []
        for j in range(m):
            temp = []
            for i in range(n):
                temp.append(A[i][j])
            B.append(temp)
                
        return B