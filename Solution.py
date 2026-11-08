class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row_count = [0] * m
        col_count = [0] * n

        # Step 1: Count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Step 2: Count communicating servers
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        count += 1

        return count