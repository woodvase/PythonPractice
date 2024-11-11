class DisjointSet:
    def __init__(self, n) -> None:
        self.__rootNode = [0] * (n + 1)
        for i in range(n + 1):
            self.__rootNode[i] = i

    def find(self, n):
        r = self.__rootNode[n]
        if r == n:
            return r
        return self.find(r)

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        self.__rootNode[rx] = ry
