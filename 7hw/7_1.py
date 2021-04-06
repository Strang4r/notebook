class Matrix:
    def __init__(self, args):
        self.args = args

    def __add__(self, other):
        summarized = []
        for i in range(len(self.args)):
            summarized.append([])
            for j in range(len(self.args[0])):
                summarized[i].append(self.args[i][j] + other.args[i][j])
        return Matrix(summarized)

    def __str__(self):
        return "\n".join(map(str, self.args))


a = [[5, 6, 7, 8],
     [6, 7, 8, 5],
     [7, 8, 5, 6],
     [8, 5, 6, 7]]

b = [[1, 2, 3, 4],
     [2, 3, 4, 1],
     [3, 4, 1, 2],
     [4, 1, 2, 3]]

c = [[99, 99, 99, 99],
     [99, 99, 99, 99],
     [99, 99, 99, 99],
     [99, 99, 99, 99]]

mat = Matrix(a)
mat0 = Matrix(b)
mat1 = Matrix(c)
print(mat + mat0 + mat1)
