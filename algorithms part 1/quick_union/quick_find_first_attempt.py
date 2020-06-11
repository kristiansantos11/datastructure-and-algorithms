class QuickFindUF:
    def __init__(self, N):
        self.node_id = [x for x in range(0, N)]

    def connected(self, p, q):
        return self.node_id[p] == self.node_id[q]

    def union(self, p, q):
        pid = self.node_id[p]
        qid = self.node_id[q]

        for i in range(0, len(self.node_id)):
            if (self.node_id[i] == pid): self.node_id[i] = qid

test = QuickFindUF(10)
print(test.node_id)

test.union(1,3)
print(test.node_id)
print(test.connected(1,3))

test.union(3,9)
print(test.node_id)
print(test.connected(9,1))

#   This is slow because it has to check the entire array every time theres
#   a union.
