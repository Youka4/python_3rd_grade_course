import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = np.array(data)
        self.rows, self.cols = self.data.shape

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Wrong dimensions")
        return Matrix(np.add(self.data, other.data))

    def __sub__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Wrong dimensions")
        return Matrix(np.subtract(self.data, other.data))

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Wrong dimensions")
        return Matrix(np.multiply(self.data, other.data))

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Wrong dimensions")
        return Matrix(np.matmul(self.data, other.data))

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

    def __str__(self):
        return np.array_str(self.data)


if __name__ == "__main__":
    np.random.seed(0)
    matrix_a = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix_b = Matrix(np.random.randint(0, 10, (10, 10)))

    result_add = matrix_a + matrix_b
    result_mul = matrix_a * matrix_b
    result_matmul = matrix_a @ matrix_b

    matrix_a.save_to_file('artifacts/task2/matrix_a.txt')
    matrix_b.save_to_file('artifacts/task2/matrix_b.txt')
    result_add.save_to_file('artifacts/task2/matrix+.txt')
    result_mul.save_to_file('artifacts/task2/matrix_mult.txt')
    result_matmul.save_to_file('artifacts/task2/matrix@.txt')