import random


class Percolation:
    # creates an n-by-n grid, with all sites initially blocked
    def __init__(self, n):
        self.size = n
        self.open_sites = 0
        self.grid = [x for x in range(0, self.size**2)]
        self.sz = [1 for x in range(0, self.size**2)]
        self.status = [False for x in range(0, self.size**2)]

        # top virtual site is grid[self.size**2] bottom virtual site is grid[self.size**2+1]
        self.grid += [self.size**2, self.size**2+1]
        self.sz += [1, 1]
        self.status += [True, True]

    # opens the site (row, col) if it is not open already
    def open(self, grid_id):
        if not self.isOpen(grid_id):
            self.status[grid_id] = True
            self.open_sites += 1

            # Check if top node is open, then union if open
            if grid_id - self.size >= 0 and self.status[grid_id - self.size]:
                self.union(grid_id, grid_id - self.size)

            # Check if bottom node is open, then union if open
            if grid_id + self.size < self.size**2 and self.status[grid_id + self.size]:
                self.union(grid_id, grid_id + self.size)

            # Check if left node is open, then union if open
            if grid_id - 1 >= 0 and grid_id % self.size > 0 and self.status[grid_id - 1]:
                self.union(grid_id, grid_id - 1)

            # Check if right node is open, then union if open
            if grid_id + 1 < self.size**2 and grid_id % self.size < self.size - 1 and self.status[grid_id + 1]:
                self.union(grid_id, grid_id + 1)

            # Virtual top union to grid_id
            if grid_id < self.size:
                self.union(grid_id, self.size**2)

            # Virtual bottom union to grid_id
            if self.size**2 > grid_id >= self.size**2 - self.size:
                self.union(grid_id, self.size**2 + 1)

    # is the site (row, col) open?
    def isOpen(self, grid_id):
        return self.status[grid_id]

    # is the site (row, col) full?
    def isFull(self, grid_id):
        return self.root(self.size**2) == self.root(grid_id)

    # returns the number of open sites
    def numberOfOpenSites(self):
        return self.open_sites

    def root(self, grid_id):
        while grid_id != self.grid[grid_id]:
            self.grid[grid_id] = self.grid[self.grid[grid_id]]
            grid_id = self.grid[grid_id]
        return grid_id

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.grid[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.grid[j] = i
            self.sz[i] += self.sz[j]

    # does the system percolate? returns boolean
    def percolates(self):
        return self.isFull(self.size**2+1)


size = 20
percolate = Percolation(size)

while not percolate.percolates():
    x = random.randrange(0, size**2)
    percolate.open(x)

print(f"Total open sites: {percolate.numberOfOpenSites()} and the "
      f"Percolating Threshold: {percolate.numberOfOpenSites()/(size**2)}")


