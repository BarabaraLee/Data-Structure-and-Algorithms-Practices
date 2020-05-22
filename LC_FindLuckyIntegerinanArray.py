class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        :time complexity: O[n]
        :space complexity: O[1]
        """
        res_dict = {}
        
        for x in arr:
            if x not in res_dict:
                res_dict[x] = 1
            else:
                res_dict[x] += 1
                
        for x,y in res_dict.items():
            if x != y:
                res_dict.pop(x)
            
        if not res_dict:
            return -1
        else:
            return max(res_dict.keys())