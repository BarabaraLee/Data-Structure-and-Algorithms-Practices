class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        :time complexity: O(n)
        :space complexity: O(1)
        """
        if not s:
            return True
        
        if not t:
            return False 
        
        slen, tlen = len(s), len(t)
        sptr, tptr = 0, 0
        
        while sptr < slen and tptr < tlen:
            if s[sptr] == t[tptr]:
                sptr += 1
            tptr += 1
            
        return True if sptr == slen else False