# Step 1: Enqueue the rotten cells and count the number of fresh cells.
from collections import deque as de
def orangesRotting(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    rotten_cells = de()
    fresh_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                rotten_cells.appendleft((i, j))
            elif grid[i][j] == 1:
                fresh_count += 1
    print(rotten_cells)
    print(fresh_count)

    number_of_steps = 0
    # walk through the rotten cells and infect the good cells
    while len(rotten_cells) != 0:
        loop = len(rotten_cells)
        for _ in range(loop):
            i, j = rotten_cells.pop()
            print(i, j)

            # Check top:
            if i - 1 >= 0:
                if grid[i - 1][j] == 1:
                    fresh_count -= 1
                    grid[i - 1][j] = 2
                    rotten_cells.appendleft((i - 1, j))

            # check right:
            if j + 1 < len(grid[0]):
                if grid[i][j + 1] == 1:
                    fresh_count -= 1
                    grid[i][j + 1] = 2
                    rotten_cells.appendleft((i, j + 1))

            # check bottom:
            if i + 1 < len(grid):
                if grid[i + 1][j] == 1:
                    fresh_count -= 1
                    grid[i + 1][j] = 2
                    rotten_cells.appendleft((i + 1, j))

            # check Left:
            if j - 1 >= 0:
                if grid[i][j - 1] == 1:
                    fresh_count -= 1
                    grid[i][j - 1] = 2
                    rotten_cells.appendleft((i, j - 1))

        if len(rotten_cells) != 0:
            number_of_steps += 1

    return number_of_steps if fresh_count is 0 else -1


print(orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))

