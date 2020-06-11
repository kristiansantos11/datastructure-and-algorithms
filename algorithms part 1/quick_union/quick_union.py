class QuickUnionUF:
    def __init__(self, N):
        self.N = N
        self.node_id = [x for x in range(0, self.N)]

    def root(self, i):
        while (i != self.node_id[i]):
            i = self.node_id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.node_id[i] = j


test = QuickUnionUF(10)
print(test.node_id)
print(" ")
test.union(1,2)
print(test.node_id)
print(" ")
test.union(4,3)
print(test.node_id)
print(" ")
test.union(1,4)
print(test.node_id)
print(" ")
test.union(1,5)
print(test.node_id)
print(" ")
test.union(3,6)
print(test.node_id)
print(" ")
