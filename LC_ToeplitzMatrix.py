class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        :time complexity: O(n*m)
        :space complexity: O(1)
        """
        n, m = len(matrix), len(matrix[0])
        
        
        starting_pairs = [(1, j) for j in range(1, m)] + \
        [(i, 1) for i in range(1, n)]
        
        for i, j in starting_pairs:
            while i < n and j < m:
                if matrix[i][j] == matrix[i - 1][j - 1]:
                    i += 1
                    j += 1
                else: 
                    return False
                
        return True
                
                
                
# 1, 2, 3
# 2, 3, 4
# 3, 4, 5
# 4, 5, 6

# [[],
#  []]
# []

# [[1],
#  [2]]
# [[1,2,3]]