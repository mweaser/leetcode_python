class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        numberOfIslands = 0
        rows = len(grid)
        cols = len(grid[0])
            
        
        def bfs(r,c):
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
             
    
            while q:
                row, col = q.popleft()
            
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    numberOfIslands += 1
                    
        return numberOfIslands
        
        