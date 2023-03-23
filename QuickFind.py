class QuickFind:
    def __init__(self, n):
        self.id = list(range(n))

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid


qf = QuickFind(10)
qf.union(5, 6)
qf.union(7, 8)
qf.union(6, 7)
print(qf.connected(5, 8))