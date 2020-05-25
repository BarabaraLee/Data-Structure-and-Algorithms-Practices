class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        :time complexit: O(n)
        :space complexity: O(n)
        """

        time = [x % 60 for x in time]
        
        cnt = 0
        dic = {}
        res = 0
        for i in range(len(time)):
            if time[i] == 0:
                cnt += 1
                
            if 60 - time[i] in dic:
                res += len(dic[60 - time[i]])
            if time[i] not in dic:
                dic[time[i]] = [i]
            else:
                dic[time[i]].append(i)
                
        return res + cnt * (cnt-1) / 2
        
        
        
# time:  30, 20, 30, 40, 40, 30
# index: 0,  1,  2,  3,  4,  5
#       
# index = 0: dic[30] = [0]
#         1: dic[20] = [1]     
#         2: dic[30] = [0,2]     res += [(0, 2)] =>1
#         3: dic[40] = [3]       res += [(1, 3)] =>1
#         4: dic[40] = [3, 4]    res += [(1, 4)] =>1
#         5: dic[30] = [0, 2, 5] res += [(0, 5), (2, 5)] =>2
            