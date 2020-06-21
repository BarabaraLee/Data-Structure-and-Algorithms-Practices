class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        :time complexity: O(n)
        :space complexity: O(1)
        """
        cnt, p1, p2 = 0, 0, 1
        res_list = []
        
        while p2 <= len(S) - 1:
            if S[p2] != S[p1]:
                if p2 -1 - p1 >=2:
                    res_list.append([p1,p2-1])
                p1 = p2
                cnt = 0
            else:
                p2 += 1
                cnt += 1
        
        if S[p2-1] == S[p1] and p2 - 1 - p1 >= 2:
            res_list.append([p1, p2-1])
        
        return res_list