import QuickUnion as uf

class UFSuccessorWithDel:
    def __init__(self, N):
        self.N = N
        self.data = [True for x in range(0, self.N)]
        self.QUUF = uf.QuickUnionUF(self.N)

    def remove(self, x):
        self.data[x] = False
        if x > 0 and not self.data[x - 1]:
            self.QUUF.union(x, x - 1)
        if x < self.N - 1 and not self.data[x + 1]:
            self.QUUF.union(x, x + 1)

    def successor(self, x):
        if self.data[x]:
            return x
        else:
            res = self.QUUF.find(x) + 1
            if res >= self.N:
                print("Error, no successor can be found.")
                return -1
            else:
                return res


test = UFSuccessorWithDel(10)
test.remove(2)
print(test.successor(1) == 2)
print(test.successor(2) == 3)
test.remove(3)
print(test.successor(2) == 4)
print(test.successor(8) == 8)
test.remove(8)
print(test.successor(8) == -1)
