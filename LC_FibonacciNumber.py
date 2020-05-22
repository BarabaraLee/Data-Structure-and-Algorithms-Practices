class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(1)
        """
        
        if N == 0:
            return 0
        if N == 1:
            return 1
        x1 = 0
        x2 = 1
        x = None
        for i in range(2,N+1):
            x = x1 + x2
            x1, x2 = x2, x

        return x
    
#     def fib2(self, N):
#         """
#         :type N: int
#         :rtype: int
#         :time complexity: O(n)
#         :space complexity: O(n)
#         """    
#         dic = {}
        
#         def fib_helper(N, dic):
#             if N in dic:
#                 return dic[N]
            
#             if N == 0:
#                 return 0
            
#             if N == 1:
#                 return 1
            
#             res = fib_helper(N - 1, dic) + fib_helper(N - 2, dic)
#             dic[N] = res
            
#             return res
        
#         return fib_helper(N, dic)