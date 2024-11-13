from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not len(grid):
            return 0
        ans = 0
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row = len(grid)
        col = len(grid[0])
        state = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and state[i][j] == 0:
                    ans += 1
                    q = [(i, j)]
                    while len(q):
                        cur = q.pop()
                        state[cur[0]][cur[1]] = 1
                        for r, c in dir:
                            nr = cur[0] + r
                            nc = cur[1] + c
                            if nr >= 0 and nr < row and nc >= 0 and nc < col and state[nr][nc] == 0 and grid[nr][nc] == "1":
                                q.append((nr, nc))
        return ans

    def numIslandsDfs(self, grid: List[List[str]]) -> int:
        if not len(grid):
            return 0
        ans = 0
        row = len(grid)
        col = len(grid[0])
        state = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if state[i][j] == 0 and grid[i][j] == "1":
                    ans += 1
                    self.helper(i, row, j, col, grid, state)
        return ans

    def helper(self, r, row, c, col, grid, state):
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if r < 0 or r >= row or c < 0 or c >= col or state[r][c] == 1 or grid[r][c] != "1":
            return
        state[r][c] = 1
        for dr, dc in dir:
            nr = r + dr
            nc = c + dc
            self.helper(nr, row, nc, col, grid, state)


print(
    Solution().numIslandsDfs(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
