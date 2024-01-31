class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIsland = 0
        row = len(grid)
        col = len(grid[0])

        def bfs(x,y):
            delta = [(0,1),(1,0),(0,-1),(-1,0)]
            grid[x][y] = "-1"
            queue = deque()
            queue.append((x,y))

            while(queue):
                cur_x, cur_y = queue.popleft()

                for dx, dy in delta:
                    next_x = cur_x + dx
                    next_y = cur_y + dy

                    if 0 <= next_x and next_x < row and 0 <= next_y and next_y < col:
                        if grid[next_x][next_y] == "1":
                            grid[next_x][next_y] = "-1"
                            queue.append((next_x, next_y))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    bfs(i,j)
                    numOfIsland += 1
        print(grid)
        return numOfIsland