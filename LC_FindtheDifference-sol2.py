class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        :time complexity: O(n)
        :space complexity: O(n)
        """
        from collections import Counter
        
        s = Counter(s)
        t = Counter(t)
        
        if len(t) > len(s):
            res = (set(t.keys()) - set(s.keys())).pop()
        else:
            for k in s:
                if s[k]!=t[k]:
                    res = k
            
        return res