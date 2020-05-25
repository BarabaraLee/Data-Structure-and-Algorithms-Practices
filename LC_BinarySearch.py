class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        :time complexity: o(log(n))
        :space complexity: o(1)
        """
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                return mid
                
        return -1