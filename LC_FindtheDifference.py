class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        :time complexity: O(n*log(n))
        :space complexity: O(1)
        """
        s = sorted(s)
        t = sorted(t)
        
        i, j = 0, 0
        while i < len(s):
            if s[i] != t[j]:
                return t[j]
            i += 1
            j += 1
            
            
        return t[len(s)]