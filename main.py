# U  uzytecznosc
# R funkcja nagrody
# discounting = 0 przecenianie
# a action
# s  punkt startowy


class ValueIterateAlgorithm():
    def __init__(self, N, M, R, d, s, A, B):
        self.A = A
        self.B = B
        self.discounting = d
        self.N = N
        self.M = M
        self.U = [[0 for i in range(N)] for j in range(M)]
        self.newU = list(self.U)
        self.R = R
        self.a = 'UP DOWN LEFT RIGHT'.split()
        self.x = s[0]
        self.y = s[1]

    def usability_table(self):
        for i in range(self.M):
            for j in range(self.N):
                if self.R[i][j] == '*':
                    self.usability((j, i))
                elif self.R[i][j] == '.':
                    self.newU[i][j] = 0
                else:
                    self.newU[i][j] = int(R[i][j])
        self.newU, self.U = self.U, self.newU

    def usability(self, s):
        x, y = s[0], s[1]
        self.newU[y][x] = round(self.value_of_R(x, y) + self.discounting * max([sum([p * self.U[np[1]][np[0]] for np, p in self.outcomes(a, x, y)]) for a in self.a]), 3)

    def outcomes(self, a, x, y):
        if a == "UP":
            n = self.neighbours(x, y)
            return [(n[1], self.A), (n[0], self.B), (n[3], self.A)]
        if a == "LEFT":
            n = self.neighbours(x, y)
            return [(n[2], self.A), (n[1], self.B), (n[0], self.A)]
        if a == "DOWN":
            n = self.neighbours(x, y)
            return [(n[3], self.A), (n[2], self.B), (n[1], self.A)]
        if a == "RIGHT":
            n = self.neighbours(x, y)
            return [(n[0], self.A), (n[3], self.B), (n[2], self.A)]

    def neighbours(self, x, y):
        """
        return [up, left, down, right]
        """
        res = []
        if x == 0 and y == 0:
            res = [(x, y), (x, y), (x, y + 1), (x + 1, y)]
        elif x == self.N - 1 and y == self.M - 1:
            res = [(x, y - 1), (x - 1, y), (x, y), (x, y)]
        elif x == 0 and y == self.M - 1:
           res = [(x, y - 1), (x, y), (x, y), (x + 1, y)]
        elif x == self.N - 1 and y == 0:
            res = [(x, y), (x - 1, y), (x, y + 1), (x, y)]
        elif x == 0:
            res = [(x, y - 1), (x, y), (x, y + 1), (x + 1, y)]
        elif y == 0:
            res = [(x, y), (x - 1, y), (x, y + 1), (x + 1, y)]
        elif x == self.N - 1:
            res = [(x, y - 1), (x - 1, y), (x, y + 1), (x, y)]
        elif y == self.M - 1:
            res = [(x, y - 1), (x - 1, y), (x, y), (x + 1, y)]
        else:
            res = [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]
        return [i if self.R[i[1]][i[0]] != '.' else (x, y) for i in res]


    def value_of_R(self, x, y):
        if self.R[y][x] == '*':
            return -0.04
        elif self.R[y][x] == '.':
            return 0
        else:
            return int(R[y][x])


print '----------'
R = [
    ['*', '*', '*', '1'],
    ['*', '.', '*', '-1'],
    ['*', '*', '*', '*'],
]
obj = ValueIterateAlgorithm(4, 3, R, 0.99, (0, 0), 0.1, 0.8)
for i in range(20):
    obj.usability_table()
    print obj.U