class UF:
    def __init__(self, N):
        self.N = N
        self.con_com = [[r] for r in range(0, self.N)]

    def union(self, p, q):
        n1 = next(((i, nodes.index(p))
            for i, nodes in enumerate(self.con_com)
            if p in nodes), None)
        n2 = next(((i, nodes.index(q))
            for i, nodes in enumerate(self.con_com)
            if q in nodes), None)
        if n1[0] == n2[0]:
            print("You cannot connect a node to itself!")
        elif (any(p in x for x in self.con_com)):
            if (any(q in y for y in self.con_com)):
                
                self.con_com.append(self.con_com[n1[0]] + self.con_com[n2[0]])
                
                self.con_com.pop(n1[0])
                
                n2 = next(((i, nodes.index(q))
                    for i, nodes in enumerate(self.con_com)
                    if q in nodes), None)
                
                self.con_com.pop(n2[0])
                
                self.N -= 1

    def connected(self, p, q):
        n1 = next(((i, nodes.index(p))
            for i, nodes in enumerate(self.con_com)
            if p in nodes), None)
        n2 = next(((i, nodes.index(q))
            for i, nodes in enumerate(self.con_com)
            if q in nodes), None)
        if n1[0] == n2[0]: return True
        else: return False
        

test = UF(10)
print(test.con_com)
test.union(1,2)
print(test.con_com)
test.union(1,3)
print(test.con_com)
test.union(2,4)
print(test.con_com)
test.union(9,4)
print(test.con_com)

print(test.connected(9,1))

sample = [[1,2],[3,4]]

print(any(3 in x for x in sample))
