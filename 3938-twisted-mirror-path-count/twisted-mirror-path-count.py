class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        MOD = 10**9 + 7

        @cache
        def dfs(row, col, d):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            if row == rows - 1 and col == cols - 1:
                return 1
            
            if grid[row][col]:
                if d == 0:  
                    return dfs(row + 1, col, 1)
                else:       
                    return dfs(row, col + 1, 0)
            else:
                return (dfs(row, col + 1, 0) + dfs(row + 1, col, 1)) % MOD

        return (dfs(0, 1, 0) + dfs(1, 0, 1)) % MOD