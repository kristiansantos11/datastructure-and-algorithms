class QuickUnionUF:
    def __init__(self, N):
        self.N = N
        self.node_id = [x for x in range(0, self.N)]
        self.large = [x for x in range(0, self.N)]
        self.sz = [x//self.N+1 for x in range(0, self.N)]

    def root(self, i):
        while (i != self.node_id[i]):
            self.node_id[i] = self.node_id[self.node_id[i]]
            i = self.node_id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q): #Comments in this function is just a sample from union(6,7)
        i = self.root(p) #root of 6 is 6; i = 6
        j = self.root(q) #root of 7 is 7; j = 7
        if i == j: return
        largestP = self.large[i] #self.large[6] = 6
        largestQ = self.large[j] #self.large[7] = 8
        if (self.sz[i] < self.sz[j]): #self.sz[6] = 1; self[7] = 2; TRUE
            self.node_id[i] = j  #self.node_id[6] is now 7
            self.sz[j] += self.sz[i] #self.sz[7] is now 3
            if (largestP > largestQ): # 6 > 8? FALSE
                self.large[j] = largestP
        else:
            self.node_id[j] = i
            self.sz[i] += self.sz[j]
            if (largestQ > largestP):
                self.large[i] = largestQ
        self.N -= 1
        if self.N == 1:
            print("You can no longer union any number!")

    def find(self, i):
        return self.large[self.root(i)]
                    
                
'''
test = QuickUnionUF(10)
print(test.sz)
print(test.node_id)
print(test.large)
print(" ")
test.union(2,1)
print(test.sz)
print(test.node_id)
print(test.large)
print(" ")
test.union(4,9)
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
print(test.find(6))
print(" ")
test.union(9,6)
print(test.sz)
print(test.node_id)
print(test.large)
print(" ")
print(test.find(6))'''
