class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        Tprev3 = 0
        Tprev2 = 1
        Tprev1 = 1
        
        if n == 0:
            return 0
        
        if n in (1, 2):
            return 1
        
        for i in range(3, n + 1):
            Tprev3, Tprev2, Tprev1 = Tprev2, Tprev1, Tprev3 + Tprev2 + Tprev1
            
        return Tprev1
            
            
# 0, 1, 1
#    1  1  2
#       1  2  4
         