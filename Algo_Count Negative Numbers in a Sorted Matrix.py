class Solution(object):
    
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        :time complexity: O(m*log(n))
        :space complexity: O(1)
        """
        m, n = len(grid), len(grid[0])
        cnt = 0
        
        for lst in grid:
            if lst[0] < 0:
                cnt += len(lst)
            elif lst[-1]  > 0:
                continue
            else:
                left, right = 0, n - 1
                while left <= right:
                    mid = left + (right - left) // 2

                    if lst[mid] >= 0:
                        left = mid + 1
                    else:
                        right = mid - 1
                cnt += n - left
                
        return cnt
        
