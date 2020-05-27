class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :time complexity: O(n):
        :space complexity: O(n)
        """
        if not nums:
            return 0
        
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
                
        degree = max([len(vals) for vals in dic.values()])
        
        distances = [vals[-1] - vals[0] + 1 if len(vals) == degree else sys.maxsize for vals in dic.values()]
        
        return min(distances)