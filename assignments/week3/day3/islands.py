def numIslands(grid):
    if not grid:
        return 0

    visited = set()
    islands= 0
    rows, cols = len(grid), len(grid[0])
    
    def bfs(r,c):
        q = deque()
        q.append((r,c))
        visited.add((r,c))
        directions=[[1,0], [0,1], [-1,0], [0,-1]]

        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if col in range(cols) and row in range(rows) and grid[row][col]=='1' and (row,col) not in visited:
                    q.append((row,col))
                    visited.add((row,col))


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r,c)   
                islands+=1
    
    return islands