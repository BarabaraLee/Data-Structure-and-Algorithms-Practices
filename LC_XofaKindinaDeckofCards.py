class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        d={}
        for x in deck:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
                
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        return reduce(gcd, d.values()) >= 2
            
            
# Euclidean gcd algorithm:           
# a1 = q1*b1 + r1 (a1 = a, b1 = b)
# a2 = q2*b2 + r2 (a2 = b1, b2 = r1) => b1 = q2*r1 + r2
# ...
# a_{n-1} = q_{n-1}*b_{n-1} + r_{n-1}
# an = qn*bn + rn (rn = 0) -> r_{n-1} is the gcd
