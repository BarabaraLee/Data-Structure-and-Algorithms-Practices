class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(1)
        """
        # 1 0 -> 1
        # 2 0 -> 1
        # 3 0 -> 2
        # 4 0 -> 2
        # 5 0 -> 3
        
        n = len(seats)
        
        i = 0
        if seats[0] == 0:
            while i < n and seats[i] == 0:
                i+= 1
        left_1 = i
        
        j = n - 1
        if seats[n - 1] == 0:
            while j >= 0 and seats[j] == 0:
                j -= 1
        right_1 = j
        
        globalmaxl = 0
        currentmaxl = 0
        for i in range(left_1 + 1, right_1 + 1):
            if seats[i - 1] == 1 and seats[i] == 0:
                currentmaxl = 1
            elif seats[i - 1] == 0 and seats[i] == 0:
                currentmaxl += 1
            elif seats[i - 1] == 0 and seats[i] == 1:
                globalmaxl = max([currentmaxl, globalmaxl])
                
        return max([left_1, n-1-right_1, (globalmaxl + 1) // 2])