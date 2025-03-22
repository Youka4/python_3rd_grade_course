import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Wrong dimensions")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Wrong dimensions")
        result = [
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Wrong dimensions")
        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])


if __name__ == "__main__":
    np.random.seed(0)
    matrix_a = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix_b = Matrix(np.random.randint(0, 10, (10, 10)))


    result_add = matrix_a + matrix_b

    result_mul = matrix_a * matrix_b

    result_matmul = matrix_a @ matrix_b

    with open('artifacts/task1/matrix+.txt', 'w') as f:
        f.write(str(result_add))

    with open('artifacts/task1/matrix_mult.txt', 'w') as f:
        f.write(str(result_mul))

    with open('artifacts/task1/matrix@.txt', 'w') as f:
        f.write(str(result_matmul))
