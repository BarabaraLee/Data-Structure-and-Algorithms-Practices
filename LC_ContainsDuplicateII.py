class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lookup = {}
        
        for i in range(len(nums)):
            if nums[i] not in lookup:
                lookup[nums[i]] = i
            else:
                if i - lookup[nums[i]] <= k:
                    return True
                else:
                    lookup[nums[i]] = i
        return False