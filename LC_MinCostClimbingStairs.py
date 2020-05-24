class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(1)
        """
        
        prev2_step_mincost = cost[0]
        prev1_step_mincost = cost[1]
        
        for i in range(2,len(cost)):
            # take 
            prev2_step_mincost, prev1_step_mincost =\
            prev1_step_mincost, \
            min(prev2_step_mincost,prev1_step_mincost) + cost[i]
            
        return min(prev2_step_mincost, prev1_step_mincost)