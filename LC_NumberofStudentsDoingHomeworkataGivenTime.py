class Solution(object):
    
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        :time complexity: O(n)
        :space complexity: O(1)
        """
        cnt = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and queryTime <= endTime[i]:
                cnt += 1
                
        return cnt   