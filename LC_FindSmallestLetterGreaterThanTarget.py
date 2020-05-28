class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        :time complexity: O(log(n))
        :space complexity: O(1)
        """
        
        
        # if letters[-1] <= target or letters[0] > target:
        #     return letters[0]
            
        start, end = 0, len(letters) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target < letters[mid]:
                end = mid - 1
            elif target >= letters[mid]:
                start = mid + 1
        
        return letters[start % len(letters)]
            
        