class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        :time complexity: O(n)
        :space complexity: O(1)
        """
            
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if i - 2 < 0 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                elif nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
                cnt += 1
                
        return True if cnt >= 1 else False
                
                
# 4, 5, 2, 6
# 1, 4, 2, 5