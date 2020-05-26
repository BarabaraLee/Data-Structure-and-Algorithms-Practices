class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev2_numways = 1
        prev1_numways = 1
        
        for i in range(2, n):
            prev2_numways, prev1_numways = \
            prev1_numways, prev1_numways + prev2_numways
            
        return 1 if n == 1 else prev2_numways + prev1_numways
        
        
# 1, 2, 3, 4, 5
# 1  1
#    1  2
#       2  3
#          3  5