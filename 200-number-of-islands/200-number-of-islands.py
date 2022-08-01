class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0 
        
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]    
            
            while queue:
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == "1":
                        queue.append((r,c))
                        visited.add((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    count += 1
        return count
                
        