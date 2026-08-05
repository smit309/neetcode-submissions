class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        perimeter = 0

        def bfs(r, c):
            nonlocal perimeter
            q = collections.deque([(r, c)])
            visit.add((r, c))

            while q:
                row, col = q.popleft()

                directions = [(0,1), (0,-1), (1,0), (-1,0)]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        perimeter += 1
                    elif grid[nr][nc] == 0:
                        perimeter += 1
                    elif (nr, nc) not in visit:
                        visit.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    bfs(r, c)
                    return perimeter
