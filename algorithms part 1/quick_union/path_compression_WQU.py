class QuickUnionUF:
    def __init__(self, N):
        self.N = N
        self.node_id = [x for x in range(0, self.N)]
        self.sz = [x//self.N+1 for x in range(0, self.N)]

    def root(self, i):
        while (i != self.node_id[i]):
            self.node_id[i] = self.node_id[self.node_id[i]]
            i = self.node_id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j: return
        if (self.sz[i] < self.sz[j]):
            self.node_id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.node_id[j] = i
            self.sz[i] += self.sz[j]

            
print(test.sz)
print(test.node_id)
print(test.large)
print(" ")
test.union(4,9)
print(test.sz)
print(test.node_id)
print(test.large)
print(" ")
test.union(1,2)
print(test.sz)
print(test.node_id)
print(test.large)
print(" ")
test.union(3,5)
print(test.sz)
print(test.node_id)
print(test.large)
print(" ")
test.union(7,8)
print(test.sz)
print(test.node_id)
print(test.large)
print(" ")
test.union(6,7)
print(test.sz)
print(test.node_id)
print(test.large)
print(" ")
test.union(9,6)
print(test.sz)
print(test.node_id)
print(test.large)
print(" ")
