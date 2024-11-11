class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        def exploreIsland(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 'W':
                return
            
            grid[row][col] = 'W'
            
            exploreIsland(row - 1, col)  
            exploreIsland(row + 1, col)  
            exploreIsland(row, col - 1)  
            exploreIsland(row, col + 1)  
        
        island_count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'L':
                    island_count += 1
                    exploreIsland(r, c)
        
        return island_count