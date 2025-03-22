import os


class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0
        self._cache = {}

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        return all(self.data[i][j] == other.data[i][j] for i in range(self.rows) for j in range(self.cols))

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

    def __hash__(self):
        return hash(tuple(tuple(sorted(row)) for row in self.data))

    def cached_matmul(self, other):
        if (hash(self), hash(other)) in self._cache:
            return self._cache[(hash(self), hash(other))]

        result = self @ other
        self._cache[(hash(self), hash(other))] = result
        return result

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])


if __name__ == "__main__":
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    C = Matrix([[2, 1], [4, 3]])
    D = Matrix([[5, 6], [7, 8]])

    print(f"Hash A: {hash(A)}")
    print(f"Hash C: {hash(C)}")

    assert hash(A) == hash(C)

    assert B == D

    result_ab = A.cached_matmul(B)
    result_cd = C.cached_matmul(D)


    assert result_ab != result_cd

    artifact_dir = 'artifacts/task3'
    os.makedirs(artifact_dir, exist_ok=True)

    with open(f'{artifact_dir}/A.txt', 'w') as f:
        f.write(str(A))

    with open(f'{artifact_dir}/B.txt', 'w') as f:
        f.write(str(B))

    with open(f'{artifact_dir}/C.txt', 'w') as f:
        f.write(str(C))

    with open(f'{artifact_dir}/D.txt', 'w') as f:
        f.write(str(D))

    with open(f'{artifact_dir}/AB.txt', 'w') as f:
        f.write(str(result_ab))

    with open(f'{artifact_dir}/CD.txt', 'w') as f:
        f.write(str(result_cd))

    with open(f'{artifact_dir}/hash.txt', 'w') as f:
        f.write(f"Hash of AB: {hash(result_ab)}\n")
        f.write(f"Hash of CD: {hash(result_cd)}\n")
