class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            stack=[(r, c)]
            while stack:
                row, col= stack.pop()
                for dr, dc in [(0,1), (1, 0), (-1, 0), (0, -1)]:
                    nr= row+dr
                    nc= col+dc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]=='1' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))

        rows= len(grid)
        cols= len(grid[0])
        visited=set()
        islands=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r, c) not in visited:
                    visited.add((r,c))
                    islands+=1   
                    dfs(r, c)         
        return islands    