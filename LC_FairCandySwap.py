class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        :time comlexity: O(len(A)+len(B))
        :space complexity: O(1)
        """
        sum_A = sum(A)
        sum_B = sum(B)
        setB = set(B)
            
        halfdiff = (sum_B - sum_A) / 2
            
        for x in A:
            if x + halfdiff in set(B):
                return [x, x + halfdiff]